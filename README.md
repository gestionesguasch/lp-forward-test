# Prueba en vivo de LP concentrado

**Actualizado:** 23/11/2026 13:05 UTC · **3.0 días de datos** · 13 lecturas · huecos: 44

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,717.39 (-0.8% desde el inicio) · mitad/mitad sin LP: -0.40%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 89% | 2 | 20.57 $ | -2.75% (-97%/año) | -1.68% (-87%/año) |
| ±5% | tras 24 h | 72% | 0 | 10.54 $ | +0.45% (+73%/año) | -2.05% (-92%/año) |
| ±10% | al salir | 100% | 0 | 13.19 $ | +0.74% (+142%/año) | -0.88% (-66%/año) |
| ±10% | tras 24 h | 100% | 0 | 13.19 $ | +0.74% (+142%/año) | -0.88% (-66%/año) |
| ±20% | al salir | 100% | 0 | 7.28 $ | +0.15% (+20%/año) | -0.56% (-49%/año) |
| ±20% | tras 24 h | 100% | 0 | 7.28 $ | +0.15% (+20%/año) | -0.56% (-49%/año) |

## BASE ETH 0.05
Precio 1,721.07 (-0.6% desde el inicio) · mitad/mitad sin LP: -0.28%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 89% | 2 | 18.95 $ | -2.70% (-96%/año) | -1.63% (-86%/año) |
| ±5% | tras 24 h | 72% | 0 | 10.70 $ | +0.74% (+142%/año) | -2.11% (-92%/año) |
| ±10% | al salir | 100% | 0 | 12.66 $ | +0.94% (+208%/año) | -0.99% (-70%/año) |
| ±10% | tras 24 h | 100% | 0 | 12.66 $ | +0.94% (+208%/año) | -0.99% (-70%/año) |
| ±20% | al salir | 100% | 0 | 6.79 $ | +0.36% (+54%/año) | -0.57% (-50%/año) |
| ±20% | tras 24 h | 100% | 0 | 6.79 $ | +0.36% (+54%/año) | -0.57% (-50%/año) |

## ARB ETH 0.05
Precio 1,721.15 (-0.6% desde el inicio) · mitad/mitad sin LP: -0.28%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 89% | 2 | 18.52 $ | -2.76% (-97%/año) | -1.69% (-87%/año) |
| ±5% | tras 24 h | 72% | 0 | 10.89 $ | +0.75% (+146%/año) | -2.11% (-92%/año) |
| ±10% | al salir | 100% | 0 | 12.38 $ | +0.91% (+197%/año) | -1.03% (-71%/año) |
| ±10% | tras 24 h | 100% | 0 | 12.38 $ | +0.91% (+197%/año) | -1.03% (-71%/año) |
| ±20% | al salir | 100% | 0 | 6.64 $ | +0.34% (+50%/año) | -0.59% (-51%/año) |
| ±20% | tras 24 h | 100% | 0 | 6.64 $ | +0.34% (+50%/año) | -0.59% (-51%/año) |

## ARB BTC 0.05
Precio 61,375.15 (-0.1% desde el inicio) · mitad/mitad sin LP: -0.03%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 94% | 1 | 11.99 $ | -1.34% (-80%/año) | -1.05% (-72%/año) |
| ±5% | tras 24 h | 81% | 0 | 8.85 $ | +0.81% (+163%/año) | -1.08% (-73%/año) |
| ±10% | al salir | 100% | 0 | 7.25 $ | +0.65% (+117%/año) | -0.48% (-44%/año) |
| ±10% | tras 24 h | 100% | 0 | 7.25 $ | +0.65% (+117%/año) | -0.48% (-44%/año) |
| ±20% | al salir | 100% | 0 | 3.88 $ | +0.31% (+45%/año) | -0.16% (-18%/año) |
| ±20% | tras 24 h | 100% | 0 | 3.88 $ | +0.31% (+45%/año) | -0.16% (-18%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
