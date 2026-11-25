# Prueba en vivo de LP concentrado

**Actualizado:** 25/11/2026 23:02 UTC · **5.5 días de datos** · 19 lecturas · huecos: 68

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,683.48 (-2.8% desde el inicio) · mitad/mitad sin LP: -1.38%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 94% | 2 | 38.43 $ | -1.83% (-71%/año) | -0.72% (-38%/año) |
| ±5% | tras 24 h | 77% | 0 | 25.67 $ | +0.63% (+52%/año) | -1.20% (-56%/año) |
| ±10% | al salir | 100% | 0 | 22.73 $ | +0.53% (+42%/año) | -0.45% (-26%/año) |
| ±10% | tras 24 h | 100% | 0 | 22.73 $ | +0.53% (+42%/año) | -0.45% (-26%/año) |
| ±20% | al salir | 100% | 0 | 12.56 $ | -0.40% (-24%/año) | -0.31% (-19%/año) |
| ±20% | tras 24 h | 100% | 0 | 12.56 $ | -0.40% (-24%/año) | -0.31% (-19%/año) |

## BASE ETH 0.05
Precio 1,679.84 (-2.9% desde el inicio) · mitad/mitad sin LP: -1.47%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 94% | 2 | 36.09 $ | -1.88% (-72%/año) | -0.81% (-42%/año) |
| ±5% | tras 24 h | 77% | 0 | 25.09 $ | +0.55% (+44%/año) | -1.23% (-56%/año) |
| ±10% | al salir | 100% | 0 | 21.75 $ | +0.44% (+34%/año) | -0.60% (-33%/año) |
| ±10% | tras 24 h | 100% | 0 | 21.75 $ | +0.44% (+34%/año) | -0.60% (-33%/año) |
| ±20% | al salir | 100% | 0 | 11.66 $ | -0.47% (-27%/año) | -0.36% (-22%/año) |
| ±20% | tras 24 h | 100% | 0 | 11.66 $ | -0.47% (-27%/año) | -0.36% (-22%/año) |

## ARB ETH 0.05
Precio 1,679.80 (-2.9% desde el inicio) · mitad/mitad sin LP: -1.47%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 94% | 2 | 36.78 $ | -1.83% (-71%/año) | -0.76% (-40%/año) |
| ±5% | tras 24 h | 77% | 0 | 26.23 $ | +0.65% (+54%/año) | -1.13% (-53%/año) |
| ±10% | al salir | 100% | 0 | 22.08 $ | +0.46% (+36%/año) | -0.57% (-32%/año) |
| ±10% | tras 24 h | 100% | 0 | 22.08 $ | +0.46% (+36%/año) | -0.57% (-32%/año) |
| ±20% | al salir | 100% | 0 | 11.84 $ | -0.46% (-26%/año) | -0.35% (-21%/año) |
| ±20% | tras 24 h | 100% | 0 | 11.84 $ | -0.46% (-26%/año) | -0.35% (-21%/año) |

## ARB BTC 0.05
Precio 60,097.66 (-2.1% desde el inicio) · mitad/mitad sin LP: -1.07%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 97% | 1 | 23.99 $ | -0.36% (-21%/año) | -0.97% (-48%/año) |
| ±5% | tras 24 h | 82% | 0 | 18.59 $ | +0.51% (+40%/año) | -1.09% (-52%/año) |
| ±10% | al salir | 100% | 0 | 13.55 $ | +0.11% (+8%/año) | -0.48% (-27%/año) |
| ±10% | tras 24 h | 100% | 0 | 13.55 $ | +0.11% (+8%/año) | -0.48% (-27%/año) |
| ±20% | al salir | 100% | 0 | 7.24 $ | -0.46% (-27%/año) | -0.17% (-11%/año) |
| ±20% | tras 24 h | 100% | 0 | 7.24 $ | -0.46% (-27%/año) | -0.17% (-11%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
