# Prueba en vivo de LP concentrado

**Actualizado:** 20/11/2026 12:15 UTC · **0.0 días de datos** · 2 lecturas · huecos: 0

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,731.23 (+0.0% desde el inicio) · mitad/mitad sin LP: +0.00%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 100% | 0 | 0.00 $ | -0.16% | -0.19% |
| ±5% | tras 24 h | 100% | 0 | 0.00 $ | -0.16% | -0.19% |
| ±10% | al salir | 100% | 0 | 0.00 $ | -0.16% | -0.19% |
| ±10% | tras 24 h | 100% | 0 | 0.00 $ | -0.16% | -0.19% |
| ±20% | al salir | 100% | 0 | 0.00 $ | -0.16% | -0.19% |
| ±20% | tras 24 h | 100% | 0 | 0.00 $ | -0.16% | -0.19% |

## BASE ETH 0.05
Precio 1,731.53 (+0.0% desde el inicio) · mitad/mitad sin LP: +0.02%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 100% | 0 | 0.01 $ | -0.01% | -0.06% |
| ±5% | tras 24 h | 100% | 0 | 0.01 $ | -0.01% | -0.06% |
| ±10% | al salir | 100% | 0 | 0.00 $ | -0.01% | -0.06% |
| ±10% | tras 24 h | 100% | 0 | 0.00 $ | -0.01% | -0.06% |
| ±20% | al salir | 100% | 0 | 0.00 $ | -0.01% | -0.06% |
| ±20% | tras 24 h | 100% | 0 | 0.00 $ | -0.01% | -0.06% |

## ARB ETH 0.05
Precio 1,731.54 (+0.0% desde el inicio) · mitad/mitad sin LP: +0.02%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 100% | 0 | 0.01 $ | -0.02% | -0.07% |
| ±5% | tras 24 h | 100% | 0 | 0.01 $ | -0.02% | -0.07% |
| ±10% | al salir | 100% | 0 | 0.00 $ | -0.02% | -0.07% |
| ±10% | tras 24 h | 100% | 0 | 0.00 $ | -0.02% | -0.07% |
| ±20% | al salir | 100% | 0 | 0.00 $ | -0.02% | -0.07% |
| ±20% | tras 24 h | 100% | 0 | 0.00 $ | -0.02% | -0.07% |

## ARB BTC 0.05
Precio 61,430.47 (+0.0% desde el inicio) · mitad/mitad sin LP: +0.01%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 100% | 0 | 0.01 $ | -0.03% | -0.07% |
| ±5% | tras 24 h | 100% | 0 | 0.01 $ | -0.03% | -0.07% |
| ±10% | al salir | 100% | 0 | 0.00 $ | -0.03% | -0.07% |
| ±10% | tras 24 h | 100% | 0 | 0.00 $ | -0.03% | -0.07% |
| ±20% | al salir | 100% | 0 | 0.00 $ | -0.03% | -0.07% |
| ±20% | tras 24 h | 100% | 0 | 0.00 $ | -0.03% | -0.07% |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
