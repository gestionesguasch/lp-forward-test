# Prueba en vivo de LP concentrado

**Actualizado:** 26/11/2026 23:44 UTC · **6.5 días de datos** · 22 lecturas · huecos: 80

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,687.26 (-2.5% desde el inicio) · mitad/mitad sin LP: -1.27%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 95% | 2 | 41.45 $ | -1.41% (-55%/año) | -0.49% (-24%/año) |
| ±5% | tras 24 h | 81% | 0 | 28.77 $ | +1.11% (+86%/año) | -0.97% (-42%/año) |
| ±10% | al salir | 100% | 0 | 24.35 $ | +0.83% (+59%/año) | -0.32% (-17%/año) |
| ±10% | tras 24 h | 100% | 0 | 24.35 $ | +0.83% (+59%/año) | -0.32% (-17%/año) |
| ±20% | al salir | 100% | 0 | 13.45 $ | -0.18% (-10%/año) | -0.22% (-12%/año) |
| ±20% | tras 24 h | 100% | 0 | 13.45 $ | -0.18% (-10%/año) | -0.22% (-12%/año) |

## BASE ETH 0.05
Precio 1,684.40 (-2.7% desde el inicio) · mitad/mitad sin LP: -1.34%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 95% | 2 | 38.75 $ | -1.49% (-57%/año) | -0.64% (-30%/año) |
| ±5% | tras 24 h | 81% | 0 | 27.79 $ | +1.03% (+78%/año) | -1.06% (-45%/año) |
| ±10% | al salir | 100% | 0 | 23.17 $ | +0.75% (+52%/año) | -0.50% (-25%/año) |
| ±10% | tras 24 h | 100% | 0 | 23.17 $ | +0.75% (+52%/año) | -0.50% (-25%/año) |
| ±20% | al salir | 100% | 0 | 12.42 $ | -0.24% (-12%/año) | -0.31% (-16%/año) |
| ±20% | tras 24 h | 100% | 0 | 12.42 $ | -0.24% (-12%/año) | -0.31% (-16%/año) |

## ARB ETH 0.05
Precio 1,684.32 (-2.7% desde el inicio) · mitad/mitad sin LP: -1.34%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 95% | 2 | 39.63 $ | -1.42% (-55%/año) | -0.58% (-28%/año) |
| ±5% | tras 24 h | 81% | 0 | 29.13 $ | +1.15% (+90%/año) | -0.94% (-41%/año) |
| ±10% | al salir | 100% | 0 | 23.59 $ | +0.78% (+55%/año) | -0.47% (-23%/año) |
| ±10% | tras 24 h | 100% | 0 | 23.59 $ | +0.78% (+55%/año) | -0.47% (-23%/año) |
| ±20% | al salir | 100% | 0 | 12.65 $ | -0.22% (-12%/año) | -0.30% (-15%/año) |
| ±20% | tras 24 h | 100% | 0 | 12.65 $ | -0.22% (-12%/año) | -0.30% (-15%/año) |

## ARB BTC 0.05
Precio 60,457.00 (-1.6% desde el inicio) · mitad/mitad sin LP: -0.78%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 97% | 1 | 25.85 $ | -0.07% (-4%/año) | -0.91% (-40%/año) |
| ±5% | tras 24 h | 85% | 0 | 20.45 $ | +1.10% (+85%/año) | -1.04% (-44%/año) |
| ±10% | al salir | 100% | 0 | 14.52 $ | +0.56% (+37%/año) | -0.45% (-23%/año) |
| ±10% | tras 24 h | 100% | 0 | 14.52 $ | +0.56% (+37%/año) | -0.45% (-23%/año) |
| ±20% | al salir | 100% | 0 | 7.76 $ | -0.08% (-5%/año) | -0.16% (-8%/año) |
| ±20% | tras 24 h | 100% | 0 | 7.76 $ | -0.08% (-5%/año) | -0.16% (-8%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
