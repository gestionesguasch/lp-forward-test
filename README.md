# Prueba en vivo de LP concentrado

**Actualizado:** 28/11/2026 14:05 UTC · **8.1 días de datos** · 27 lecturas · huecos: 100

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,638.32 (-5.4% desde el inicio) · mitad/mitad sin LP: -2.68%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 47.09 $ | -2.71% (-71%/año) | -1.61% (-52%/año) |
| ±5% | tras 24 h | 82% | 0 | 34.08 $ | -0.92% (-34%/año) | -2.14% (-62%/año) |
| ±10% | al salir | 100% | 0 | 27.36 $ | -0.88% (-33%/año) | -0.91% (-34%/año) |
| ±10% | tras 24 h | 100% | 0 | 27.36 $ | -0.88% (-33%/año) | -0.91% (-34%/año) |
| ±20% | al salir | 100% | 0 | 15.11 $ | -1.76% (-55%/año) | -0.56% (-22%/año) |
| ±20% | tras 24 h | 100% | 0 | 15.11 $ | -1.76% (-55%/año) | -0.56% (-22%/año) |

## BASE ETH 0.05
Precio 1,640.90 (-5.2% desde el inicio) · mitad/mitad sin LP: -2.59%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 44.43 $ | -2.44% (-67%/año) | -1.90% (-58%/año) |
| ±5% | tras 24 h | 82% | 0 | 33.14 $ | -0.74% (-28%/año) | -2.37% (-66%/año) |
| ±10% | al salir | 100% | 0 | 26.18 $ | -0.74% (-29%/año) | -1.16% (-41%/año) |
| ±10% | tras 24 h | 100% | 0 | 26.18 $ | -0.74% (-29%/año) | -1.16% (-41%/año) |
| ±20% | al salir | 100% | 0 | 14.03 $ | -1.62% (-52%/año) | -0.57% (-23%/año) |
| ±20% | tras 24 h | 100% | 0 | 14.03 $ | -1.62% (-52%/año) | -0.57% (-23%/año) |

## ARB ETH 0.05
Precio 1,640.90 (-5.2% desde el inicio) · mitad/mitad sin LP: -2.60%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 45.43 $ | -2.36% (-66%/año) | -1.83% (-57%/año) |
| ±5% | tras 24 h | 82% | 0 | 34.57 $ | -0.60% (-24%/año) | -2.25% (-64%/año) |
| ±10% | al salir | 100% | 0 | 26.68 $ | -0.70% (-27%/año) | -1.13% (-40%/año) |
| ±10% | tras 24 h | 100% | 0 | 26.68 $ | -0.70% (-27%/año) | -1.13% (-40%/año) |
| ±20% | al salir | 100% | 0 | 14.30 $ | -1.60% (-52%/año) | -0.55% (-22%/año) |
| ±20% | tras 24 h | 100% | 0 | 14.30 $ | -1.60% (-52%/año) | -0.55% (-22%/año) |

## ARB BTC 0.05
Precio 59,153.75 (-3.7% desde el inicio) · mitad/mitad sin LP: -1.84%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 29.12 $ | -2.75% (-72%/año) | -1.48% (-49%/año) |
| ±5% | tras 24 h | 88% | 0 | 24.05 $ | -0.18% (-8%/año) | -1.54% (-50%/año) |
| ±10% | al salir | 100% | 0 | 16.41 $ | -0.61% (-24%/año) | -0.72% (-28%/año) |
| ±10% | tras 24 h | 100% | 0 | 16.41 $ | -0.61% (-24%/año) | -0.72% (-28%/año) |
| ±20% | al salir | 100% | 0 | 8.77 $ | -1.21% (-42%/año) | -0.25% (-11%/año) |
| ±20% | tras 24 h | 100% | 0 | 8.77 $ | -1.21% (-42%/año) | -0.25% (-11%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
