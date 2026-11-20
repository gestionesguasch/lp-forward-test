#!/usr/bin/env python3
"""
lp_forward_test.py - Prueba en vivo de LP concentrado (Uniswap v3), sin cuentas ni API keys.

Que hace:
  Cada 5 minutos lee de la blockchain (RPC publicos) el estado real de 4 pools:
  precio, tick y "feeGrowthGlobal" (comisiones exactas cobradas por unidad de liquidez).
  Con eso simula posiciones VIRTUALES de 1.000 $ (no mueve dinero) con varios rangos
  y reglas de reajuste, con y sin cobertura (corto en Hyperliquid, con funding real).

Pools:
  BASE_ETH_0.30  Uniswap v3 WETH/USDC 0,30 % (Base)
  BASE_ETH_0.05  Uniswap v3 WETH/USDC 0,05 % (Base)
  ARB_ETH_0.05   Uniswap v3 WETH/USDC 0,05 % (Arbitrum)
  ARB_BTC_0.05   Uniswap v3 WBTC/USDC 0,05 % (Arbitrum)

Uso (Mac, carpeta Leverage):
  caffeinate -i python3 lp_forward_test.py        # arranca / reanuda (caffeinate evita que el Mac se duerma)
  python3 lp_forward_test.py --report             # muestra el informe sin parar la prueba
  python3 lp_forward_test.py --reset              # borra todo y empieza de cero
  python3 lp_forward_test.py --once               # una sola lectura y sale (lo usa GitHub Actions cada 5 min)

Archivos que crea (en la carpeta lp_forward_data/ junto al script):
  state.json          estado para reanudar si lo paras (Ctrl+C) o se reinicia el Mac
  samples.csv         una fila por pool cada 5 min (precio, tick, liquidez activa, comisiones)
  snapshots.csv       una fila por estrategia cada hora
  report.txt          ultimo informe

Solo usa la libreria estandar de Python. No necesita instalar nada.
"""

import csv
import json
import math
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone

# ---------------------------------------------------------------- configuracion
CAPITAL = 1000.0          # $ virtuales por estrategia
INTERVAL = 300            # segundos entre lecturas
WIDTHS = [0.05, 0.10, 0.20]                  # rango +-5 %, +-10 %, +-20 %
RULES = {"inmediato": 0, "tras24h": 24 * 3600}  # reajustar al salir del rango / tras 24 h fuera
SLIPPAGE = 0.0002         # deslizamiento extra al hacer el swap de reajuste
PERP_FEE = 0.00045        # comision taker de Hyperliquid
HEDGE_BAND = 0.05         # reajusta el corto si se desvia mas de un 5 %
REPORT_EVERY = 3600       # informe y snapshot cada hora
GAP_SECONDS = 3 * INTERVAL  # mas tiempo que esto entre lecturas cuenta como hueco

RPC = {
    "base": ["https://mainnet.base.org", "https://base-rpc.publicnode.com", "https://base.drpc.org"],
    "arbitrum": ["https://arb1.arbitrum.io/rpc", "https://arbitrum-one-rpc.publicnode.com", "https://arbitrum.drpc.org"],
}
POOLS = {
    "BASE_ETH_0.30": {"chain": "base", "addr": "0x6c561b446416e1a00e8e93e221854d6ea4171372", "gas_usd": 0.05, "hl": "ETH"},
    "BASE_ETH_0.05": {"chain": "base", "addr": "0xd0b53d9277642d899df5c87a3966a349a798f224", "gas_usd": 0.05, "hl": "ETH"},
    "ARB_ETH_0.05": {"chain": "arbitrum", "addr": "0xc6962004f452be9203591991d15f6b388e09e8d0", "gas_usd": 0.10, "hl": "ETH"},
    "ARB_BTC_0.05": {"chain": "arbitrum", "addr": "0x0e4831319a50228b9e450861297ab92dee15b44f", "gas_usd": 0.10, "hl": "BTC"},
}
STABLES = {"0x833589fcd6edb6e08f4c7c32d4f71b54bda02913", "0xaf88d065e77c8cc2239327c5edb3a432268e5831"}

SEL = {"slot0": "0x3850c7bd", "liquidity": "0x1a686502", "fg0": "0xf3058399", "fg1": "0x46141319",
       "token0": "0x0dfe1681", "token1": "0xd21220a7", "fee": "0xddca3f43", "tickSpacing": "0xd0c93a7c",
       "decimals": "0x313ce567"}

Q96 = 2 ** 96
Q128 = 2 ** 128
U256 = 2 ** 256

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "lp_forward_data")
STATE_F = os.path.join(DATA, "state.json")


# ---------------------------------------------------------------- red
def _post(url, payload, timeout=20):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 headers={"content-type": "application/json", "user-agent": "lp-forward-test/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def eth_call(chain, to, data):
    last = None
    for attempt in range(3):
        for url in RPC[chain]:
            try:
                r = _post(url, {"jsonrpc": "2.0", "id": 1, "method": "eth_call", "params": [{"to": to, "data": data}, "latest"]})
                if "result" in r and r["result"] not in (None, "0x"):
                    return r["result"]
                last = r.get("error")
            except Exception as e:  # noqa: BLE001
                last = e
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"RPC {chain} fallo: {last}")


def word(hexstr, i):
    h = hexstr[2:] if hexstr.startswith("0x") else hexstr
    return int(h[64 * i: 64 * (i + 1)], 16)


def signed24(v):
    v &= (1 << 24) - 1
    return v - (1 << 24) if v >= (1 << 23) else v


def hl_funding():
    """Funding horario actual de Hyperliquid (positivo = los largos pagan a los cortos)."""
    try:
        meta, ctx = _post("https://api.hyperliquid.xyz/info", {"type": "metaAndAssetCtxs"})
        out = {}
        for i, u in enumerate(meta["universe"]):
            if u["name"] in ("ETH", "BTC"):
                out[u["name"]] = float(ctx[i]["funding"])
        return out
    except Exception:  # noqa: BLE001
        return {}


# ---------------------------------------------------------------- matematicas Uniswap v3
def amounts(L, sp, spa, spb):
    """Cantidades raw (token0, token1) de una posicion con liquidez L."""
    if sp <= spa:
        return L * (1 / spa - 1 / spb), 0.0
    if sp >= spb:
        return 0.0, L * (spb - spa)
    return L * (1 / sp - 1 / spb), L * (sp - spa)


def tick_sqrt(t):
    return 1.0001 ** (t / 2)


class Pool:
    def __init__(self, name, cfg):
        self.name, self.cfg = name, cfg
        a, ch = cfg["addr"], cfg["chain"]
        self.t0 = "0x" + eth_call(ch, a, SEL["token0"])[-40:]
        self.t1 = "0x" + eth_call(ch, a, SEL["token1"])[-40:]
        self.d0 = int(eth_call(ch, self.t0, SEL["decimals"]), 16)
        self.d1 = int(eth_call(ch, self.t1, SEL["decimals"]), 16)
        self.fee = int(eth_call(ch, a, SEL["fee"]), 16) / 1e6
        self.ts = signed24(int(eth_call(ch, a, SEL["tickSpacing"]), 16))
        if self.t1.lower() in STABLES:
            self.stable_is_1 = True
        elif self.t0.lower() in STABLES:
            self.stable_is_1 = False
        else:
            raise RuntimeError(f"{name}: no encuentro el USDC en el pool")

    def read(self):
        a, ch = self.cfg["addr"], self.cfg["chain"]
        s0 = eth_call(ch, a, SEL["slot0"])
        sqrtp = word(s0, 0) / Q96
        tick = signed24(word(s0, 1))
        liq = int(eth_call(ch, a, SEL["liquidity"]), 16)
        fg0 = int(eth_call(ch, a, SEL["fg0"]), 16)
        fg1 = int(eth_call(ch, a, SEL["fg1"]), 16)
        return {"sqrtp": sqrtp, "tick": tick, "liq": liq, "fg0": fg0, "fg1": fg1}

    def prices(self, sqrtp):
        """Precio en $ de token0 y token1."""
        raw = sqrtp * sqrtp * 10 ** (self.d0 - self.d1)  # token1 por token0, unidades humanas
        return (raw, 1.0) if self.stable_is_1 else (1.0, 1 / raw)

    def risky_price(self, sqrtp):
        p0, p1 = self.prices(sqrtp)
        return p0 if self.stable_is_1 else p1

    def usd(self, a0_raw, a1_raw, sqrtp):
        p0, p1 = self.prices(sqrtp)
        return a0_raw / 10 ** self.d0 * p0 + a1_raw / 10 ** self.d1 * p1

    def risky_amount(self, a0_raw, a1_raw):
        return a0_raw / 10 ** self.d0 if self.stable_is_1 else a1_raw / 10 ** self.d1


# ---------------------------------------------------------------- estrategia virtual
def mint(pool, value_usd, snap, w):
    """Abre una posicion virtual de value_usd centrada en el precio actual con rango +-w."""
    sp, tick = snap["sqrtp"], snap["tick"]
    lt = math.log(1.0001)
    raw_p = sp * sp
    tl = math.floor(math.log(raw_p / (1 + w)) / lt / pool.ts) * pool.ts
    tu = math.ceil(math.log(raw_p * (1 + w)) / lt / pool.ts) * pool.ts
    if not tl <= tick < tu:  # seguridad
        tl, tu = min(tl, tick - pool.ts), max(tu, tick + pool.ts)
    a0, a1 = amounts(1.0, sp, tick_sqrt(tl), tick_sqrt(tu))
    L = value_usd / pool.usd(a0, a1, sp)
    return tl, tu, L


def new_strategy(pool, snap, w, rule):
    c0 = 0.5 * CAPITAL * (pool.fee + SLIPPAGE) + pool.cfg["gas_usd"]
    tl, tu, L = mint(pool, CAPITAL - c0, snap, w)
    sp = snap["sqrtp"]
    a0, a1 = amounts(L, sp, tick_sqrt(tl), tick_sqrt(tu))
    short = pool.risky_amount(a0, a1)
    P = pool.risky_price(sp)
    hcost = short * P * PERP_FEE
    return {"w": w, "rule": rule, "tl": tl, "tu": tu, "L": L, "fees": 0.0, "fees_total": 0.0,
            "costs": c0, "reb": 0, "out_since": None, "in_prev": True, "time_in": 0.0, "time_all": 0.0,
            "short": short, "hpnl": -hcost, "hfund": 0.0, "hcost": hcost}


def lp_value(pool, s, sp):
    a0, a1 = amounts(s["L"], sp, tick_sqrt(s["tl"]), tick_sqrt(s["tu"]))
    return pool.usd(a0, a1, sp), a0, a1


def step(pool, s, prev, snap, dt, funding_h, now):
    sp, tick = snap["sqrtp"], snap["tick"]
    in_now = s["tl"] <= tick < s["tu"]
    # 1) comisiones exactas: L x delta(feeGrowthGlobal) mientras esta en rango
    f = (int(s["in_prev"]) + int(in_now)) / 2
    if f > 0:
        d0 = (snap["fg0"] - prev["fg0"]) % U256
        d1 = (snap["fg1"] - prev["fg1"]) % U256
        fee_usd = pool.usd(s["L"] * d0 / Q128, s["L"] * d1 / Q128, sp) * f
        s["fees"] += fee_usd
        s["fees_total"] += fee_usd
    s["time_all"] += dt
    s["time_in"] += dt * f
    # 2) cobertura: PnL del corto + funding
    P_prev, P = pool.risky_price(prev["sqrtp"]), pool.risky_price(sp)
    s["hpnl"] += s["short"] * (P_prev - P)
    fund = s["short"] * P * funding_h * dt / 3600
    s["hpnl"] += fund
    s["hfund"] += fund
    # 3) regla de reajuste
    if in_now:
        s["out_since"] = None
    elif s["out_since"] is None:
        s["out_since"] = now
    rebalanced = False
    if not in_now and now - s["out_since"] >= RULES[s["rule"]]:
        val, _, _ = lp_value(pool, s, sp)
        val += s["fees"]
        c = 0.5 * val * (pool.fee + SLIPPAGE) + pool.cfg["gas_usd"]
        s["costs"] += c
        s["tl"], s["tu"], s["L"] = mint(pool, val - c, snap, s["w"])
        s["fees"] = 0.0
        s["reb"] += 1
        s["out_since"] = None
        in_now = True
        rebalanced = True
    s["in_prev"] = in_now
    # 4) reajuste del corto
    _, a0, a1 = lp_value(pool, s, sp)
    target = pool.risky_amount(a0, a1)
    if rebalanced or abs(target - s["short"]) > HEDGE_BAND * max(target, s["short"], 1e-12):
        c = abs(target - s["short"]) * P * PERP_FEE
        s["hpnl"] -= c
        s["hcost"] += c
        s["short"] = target


def totals(pool, s, sp):
    v, _, _ = lp_value(pool, s, sp)
    unhedged = v + s["fees"]
    return unhedged, unhedged + s["hpnl"]


# ---------------------------------------------------------------- informe
def ann(v, days):
    if days < 1 or v <= 0:
        return None
    return ((v / CAPITAL) ** (365 / days) - 1) * 100


def fmt_pct(x):
    return "   -   " if x is None else f"{x:+7.1f}%"


def report(state, pools):
    now = time.time()
    lines = []
    days = (now - state["start"]) / 86400
    lines.append(f"PRUEBA EN VIVO DE LP  |  {datetime.now().strftime('%d/%m/%Y %H:%M')}  |  "
                 f"{days:.2f} dias de datos  |  {state['samples']} lecturas  |  huecos: {state['gaps']}")
    lines.append(f"Capital virtual por estrategia: {CAPITAL:.0f} $. Anualizado solo a partir de 1 dia "
                 f"(con pocos dias exagera mucho: mira tambien el %).")
    lines.append("")
    for pname, pool in pools.items():
        ps = state["pools"].get(pname)
        if not ps or "last" not in ps:
            continue
        sp = ps["last"]["sqrtp"]
        P, P0 = pool.risky_price(sp), ps["p0"]
        hodl = CAPITAL / 2 + CAPITAL / 2 * P / P0
        lines.append(f"== {pname}  precio {P:,.2f} ({(P / P0 - 1) * 100:+.1f}% desde el inicio)  |  "
                     f"mitad/mitad: {hodl:,.0f} $ ({(hodl / CAPITAL - 1) * 100:+.1f}%)")
        lines.append(f"   {'rango':>6} {'regla':>9} | {'en rango':>8} {'reaj':>4} {'comis.':>8} {'costes':>7} | "
                     f"{'SIN cobertura':>22} | {'CON cobertura':>22} {'funding':>8}")
        for key, s in ps["strats"].items():
            u, h = totals(pool, s, sp)
            tin = s["time_in"] / s["time_all"] * 100 if s["time_all"] else 100
            lines.append(
                f"   +-{s['w'] * 100:>3.0f}% {s['rule']:>9} | {tin:>7.0f}% {s['reb']:>4} "
                f"{s['fees_total']:>7.2f}$ {s['costs'] + s['hcost']:>6.2f}$ | "
                f"{u:>8.1f}$ {(u / CAPITAL - 1) * 100:+6.2f}% {fmt_pct(ann(u, days))} | "
                f"{h:>8.1f}$ {(h / CAPITAL - 1) * 100:+6.2f}% {fmt_pct(ann(h, days))} {s['hfund']:>+7.2f}$")
        lines.append("")
    lines.append("Como leerlo: 'comis.' = comisiones reales cobradas; 'CON cobertura' = LP + corto en Hyperliquid")
    lines.append("(quita la direccion del precio; necesitarias ~30 % extra de margen para el corto).")
    lines.append("Lo que buscamos: CON cobertura positivo y estable durante 2-3 semanas.")
    txt = "\n".join(lines)
    with open(os.path.join(DATA, "report.txt"), "w") as f:
        f.write(txt + "\n")
    return txt


def snapshot_rows(state, pools):
    path = os.path.join(DATA, "snapshots.csv")
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["utc", "pool", "rango", "regla", "precio", "en_rango_pct", "reajustes",
                        "comisiones_usd", "costes_usd", "valor_sin_cobertura", "valor_con_cobertura", "funding_usd"])
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
        for pname, pool in pools.items():
            ps = state["pools"].get(pname)
            if not ps or "last" not in ps:
                continue
            sp = ps["last"]["sqrtp"]
            for s in ps["strats"].values():
                u, h = totals(pool, s, sp)
                tin = s["time_in"] / s["time_all"] * 100 if s["time_all"] else 100
                w.writerow([ts, pname, f"{s['w']:.2f}", s["rule"], f"{pool.risky_price(sp):.2f}", f"{tin:.1f}",
                            s["reb"], f"{s['fees_total']:.4f}", f"{s['costs'] + s['hcost']:.4f}",
                            f"{u:.4f}", f"{h:.4f}", f"{s['hfund']:.4f}"])


def log_sample(pname, pool, snap, prev):
    path = os.path.join(DATA, "samples.csv")
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["utc", "pool", "precio", "tick", "liquidez_activa", "comis_usd_por_1000usd_en_rango_intervalo"])
        per1k = ""
        if prev:
            # comisiones del intervalo para 1000 $ en un rango de +-10 % (referencia comparable entre pools)
            tl, tu, L = mint(pool, 1000.0, snap, 0.10)
            d0 = (snap["fg0"] - prev["fg0"]) % U256
            d1 = (snap["fg1"] - prev["fg1"]) % U256
            per1k = f"{pool.usd(L * d0 / Q128, L * d1 / Q128, snap['sqrtp']):.6f}"
        w.writerow([datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"), pname,
                    f"{pool.risky_price(snap['sqrtp']):.4f}", snap["tick"], snap["liq"], per1k])



def write_readme(state, pools):
    """Informe en Markdown para la portada del repositorio (se lee bien desde el móvil)."""
    now = time.time()
    days = (now - state["start"]) / 86400
    upd = datetime.now(timezone.utc).strftime("%d/%m/%Y %H:%M UTC")
    L = ["# Prueba en vivo de LP concentrado", "",
         f"**Actualizado:** {upd} · **{days:.1f} días de datos** · {state['samples']} lecturas · huecos: {state['gaps']}", "",
         "Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones "
         f"virtuales de {CAPITAL:.0f} $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto "
         "en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).", "",
         "Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir "
         "de 1 día y con pocos dias exagera: fíjate tambien en el %.", ""]
    for pname, pool in pools.items():
        ps = state["pools"].get(pname)
        if not ps or "last" not in ps:
            continue
        sp = ps["last"]["sqrtp"]
        P, P0 = pool.risky_price(sp), ps["p0"]
        hodl = CAPITAL / 2 + CAPITAL / 2 * P / P0
        L.append(f"## {pname.replace('_', ' ')}")
        L.append(f"Precio {P:,.2f} ({(P / P0 - 1) * 100:+.1f}% desde el inicio) · mitad/mitad sin LP: {(hodl / CAPITAL - 1) * 100:+.2f}%")
        L.append("")
        L.append("| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |")
        L.append("|---|---|---|---|---|---|---|")
        for s in ps["strats"].values():
            u, h = totals(pool, s, sp)
            tin = s["time_in"] / s["time_all"] * 100 if s["time_all"] else 100
            au, ah = ann(u, days), ann(h, days)
            fu = f"{(u / CAPITAL - 1) * 100:+.2f}%" + (f" ({au:+.0f}%/año)" if au is not None else "")
            fh = f"{(h / CAPITAL - 1) * 100:+.2f}%" + (f" ({ah:+.0f}%/año)" if ah is not None else "")
            regla = "al salir" if s["rule"] == "inmediato" else "tras 24 h"
            L.append(f"| ±{s['w'] * 100:.0f}% | {regla} | {tin:.0f}% | {s['reb']} | {s['fees_total']:.2f} $ | {fu} | {fh} |")
        L.append("")
    L += ["---", "Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). "
          "Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`)."]
    with open(os.path.join(HERE, "README.md"), "w") as f:
        f.write("\n".join(L) + "\n")

# ---------------------------------------------------------------- estado
def to_json(state):
    out = json.loads(json.dumps(state, default=str))
    for ps in out["pools"].values():
        if "last" in ps:
            ps["last"] = {k: str(v) if k in ("fg0", "fg1", "liq") else v for k, v in ps["last"].items()}
    return out


def from_json(d):
    for ps in d["pools"].values():
        if "last" in ps:
            for k in ("fg0", "fg1", "liq"):
                ps["last"][k] = int(ps["last"][k])
    return d


def save(state):
    tmp = STATE_F + ".tmp"
    with open(tmp, "w") as f:
        json.dump(to_json(state), f)
    os.replace(tmp, STATE_F)


def load():
    if os.path.exists(STATE_F):
        with open(STATE_F) as f:
            return from_json(json.load(f))
    return None


# ---------------------------------------------------------------- bucle principal
def init_pools():
    pools = {}
    for name, cfg in POOLS.items():
        try:
            pools[name] = Pool(name, cfg)
            p = pools[name]
            print(f"  {name}: fee {p.fee * 100:.2f}%  tickSpacing {p.ts}")
        except Exception as e:  # noqa: BLE001
            print(f"  {name}: no disponible ahora ({e}). Se omite.")
    return pools


def tick_once(state, pools):
    now = time.time()
    funding = hl_funding()
    for pname, pool in pools.items():
        try:
            snap = pool.read()
        except Exception as e:  # noqa: BLE001
            print(f"  [{datetime.now().strftime('%H:%M')}] {pname}: lectura fallida ({e}); lo reintento en la siguiente.")
            continue
        ps = state["pools"].setdefault(pname, {})
        prev = ps.get("last")
        log_sample(pname, pool, snap, prev)
        if prev is None:
            ps["p0"] = pool.risky_price(snap["sqrtp"])
            ps["strats"] = {f"{w}|{r}": new_strategy(pool, snap, w, r) for w in WIDTHS for r in RULES}
        else:
            dt = now - ps["t"]
            if dt > GAP_SECONDS:
                state["gaps"] += 1
            fh = funding.get(pool.cfg["hl"], 0.0)
            for s in ps["strats"].values():
                step(pool, s, prev, snap, dt, fh, now)
        ps["last"], ps["t"] = snap, now
    state["samples"] += 1
    save(state)


def main():
    os.makedirs(DATA, exist_ok=True)
    args = sys.argv[1:]
    if "--reset" in args:
        for fn in ("state.json", "samples.csv", "snapshots.csv", "report.txt"):
            p = os.path.join(DATA, fn)
            if os.path.exists(p):
                os.remove(p)
        print("Datos borrados. Vuelve a ejecutar sin --reset para empezar.")
        return
    print("Conectando con los pools...")
    pools = init_pools()
    if not pools:
        print("No he podido leer ningun pool. Revisa la conexion a internet.")
        return
    state = load()
    if "--report" in args:
        print(report(state, pools) if state else "Todavia no hay datos.")
        return
    if "--once" in args:
        global GAP_SECONDS
        GAP_SECONDS = 30 * 60  # GitHub Actions no es puntual; solo cuenta como hueco si pasan >30 min
        if state is None:
            state = {"start": time.time(), "samples": 0, "gaps": 0, "pools": {}, "last_report": 0}
        tick_once(state, pools)
        if time.time() - state.get("last_report", 0) >= REPORT_EVERY:
            snapshot_rows(state, pools)
            report(state, pools)
            state["last_report"] = time.time()
            save(state)
        write_readme(state, pools)
        print(f"Lectura {state['samples']} ok")
        return
    if state is None:
        state = {"start": time.time(), "samples": 0, "gaps": 0, "pools": {}, "last_report": 0}
        print("Empiezo una prueba nueva.")
    else:
        print(f"Reanudo la prueba ({(time.time() - state['start']) / 86400:.2f} dias de datos).")
    print(f"Leo cada {INTERVAL // 60} min. Informe cada hora. Ctrl+C para parar (se guarda todo).\n")
    try:
        while True:
            t0 = time.time()
            tick_once(state, pools)
            if time.time() - state.get("last_report", 0) >= REPORT_EVERY:
                print(report(state, pools))
                print()
                snapshot_rows(state, pools)
                state["last_report"] = time.time()
                save(state)
            else:
                print(f"  [{datetime.now().strftime('%H:%M')}] lectura {state['samples']} ok")
            time.sleep(max(5, INTERVAL - (time.time() - t0)))
    except KeyboardInterrupt:
        save(state)
        print("\nParado. Todo guardado. Vuelve a ejecutarlo para continuar donde lo dejaste.")


if __name__ == "__main__":
    main()
