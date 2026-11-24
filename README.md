# Prueba en vivo de LP concentrado

**Actualizado:** 24/11/2026 00:48 UTC · **3.5 días de datos** · 14 lecturas · huecos: 48

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,706.96 (-1.4% desde el inicio) · mitad/mitad sin LP: -0.70%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 91% | 2 | 26.61 $ | -2.37% (-92%/año) | -1.10% (-68%/año) |
| ±5% | tras 24 h | 76% | 0 | 16.73 $ | +0.70% (+107%/año) | -1.45% (-78%/año) |
| ±10% | al salir | 100% | 0 | 16.41 $ | +0.72% (+111%/año) | -0.58% (-45%/año) |
| ±10% | tras 24 h | 100% | 0 | 16.41 $ | +0.72% (+111%/año) | -0.58% (-45%/año) |
| ±20% | al salir | 100% | 0 | 9.06 $ | +0.01% (+1%/año) | -0.39% (-33%/año) |
| ±20% | tras 24 h | 100% | 0 | 9.06 $ | +0.01% (+1%/año) | -0.39% (-33%/año) |

## BASE ETH 0.05
Precio 1,707.84 (-1.3% desde el inicio) · mitad/mitad sin LP: -0.66%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 91% | 2 | 23.97 $ | -2.42% (-92%/año) | -1.17% (-70%/año) |
| ±5% | tras 24 h | 76% | 0 | 15.81 $ | +0.79% (+126%/año) | -1.65% (-82%/año) |
| ±10% | al salir | 100% | 0 | 15.33 $ | +0.79% (+125%/año) | -0.75% (-54%/año) |
| ±10% | tras 24 h | 100% | 0 | 15.33 $ | +0.79% (+125%/año) | -0.75% (-54%/año) |
| ±20% | al salir | 100% | 0 | 8.21 $ | +0.10% (+11%/año) | -0.43% (-36%/año) |
| ±20% | tras 24 h | 100% | 0 | 8.21 $ | +0.10% (+11%/año) | -0.43% (-36%/año) |

## ARB ETH 0.05
Precio 1,707.80 (-1.3% desde el inicio) · mitad/mitad sin LP: -0.66%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 91% | 2 | 23.98 $ | -2.44% (-92%/año) | -1.19% (-71%/año) |
| ±5% | tras 24 h | 76% | 0 | 16.44 $ | +0.84% (+139%/año) | -1.60% (-81%/año) |
| ±10% | al salir | 100% | 0 | 15.28 $ | +0.78% (+123%/año) | -0.77% (-55%/año) |
| ±10% | tras 24 h | 100% | 0 | 15.28 $ | +0.78% (+123%/año) | -0.77% (-55%/año) |
| ±20% | al salir | 100% | 0 | 8.19 $ | +0.09% (+9%/año) | -0.44% (-37%/año) |
| ±20% | tras 24 h | 100% | 0 | 8.19 $ | +0.09% (+9%/año) | -0.44% (-37%/año) |

## ARB BTC 0.05
Precio 61,272.56 (-0.2% desde el inicio) · mitad/mitad sin LP: -0.12%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 95% | 1 | 15.27 $ | -1.01% (-65%/año) | -0.73% (-53%/año) |
| ±5% | tras 24 h | 83% | 0 | 12.13 $ | +1.05% (+195%/año) | -0.74% (-54%/año) |
| ±10% | al salir | 100% | 0 | 8.97 $ | +0.73% (+113%/año) | -0.30% (-27%/año) |
| ±10% | tras 24 h | 100% | 0 | 8.97 $ | +0.73% (+113%/año) | -0.30% (-27%/año) |
| ±20% | al salir | 100% | 0 | 4.80 $ | +0.32% (+39%/año) | -0.06% (-6%/año) |
| ±20% | tras 24 h | 100% | 0 | 4.80 $ | +0.32% (+39%/año) | -0.06% (-6%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
