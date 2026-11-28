# Prueba en vivo de LP concentrado

**Actualizado:** 28/11/2026 05:00 UTC · **7.7 días de datos** · 26 lecturas · huecos: 96

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,665.01 (-3.8% desde el inicio) · mitad/mitad sin LP: -1.91%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 46.19 $ | -1.68% (-55%/año) | -1.60% (-53%/año) |
| ±5% | tras 24 h | 84% | 0 | 33.62 $ | +0.53% (+29%/año) | -2.10% (-63%/año) |
| ±10% | al salir | 100% | 0 | 26.88 $ | +0.22% (+11%/año) | -0.91% (-35%/año) |
| ±10% | tras 24 h | 100% | 0 | 26.88 $ | +0.22% (+11%/año) | -0.91% (-35%/año) |
| ±20% | al salir | 100% | 0 | 14.85 $ | -0.81% (-32%/año) | -0.56% (-23%/año) |
| ±20% | tras 24 h | 100% | 0 | 14.85 $ | -0.81% (-32%/año) | -0.56% (-23%/año) |

## BASE ETH 0.05
Precio 1,661.01 (-4.0% desde el inicio) · mitad/mitad sin LP: -2.01%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 43.58 $ | -1.74% (-56%/año) | -1.91% (-60%/año) |
| ±5% | tras 24 h | 84% | 0 | 32.71 $ | +0.36% (+19%/año) | -2.34% (-68%/año) |
| ±10% | al salir | 100% | 0 | 25.73 $ | +0.09% (+4%/año) | -1.17% (-43%/año) |
| ±10% | tras 24 h | 100% | 0 | 25.73 $ | +0.09% (+4%/año) | -1.17% (-43%/año) |
| ±20% | al salir | 100% | 0 | 13.79 $ | -0.91% (-35%/año) | -0.58% (-24%/año) |
| ±20% | tras 24 h | 100% | 0 | 13.79 $ | -0.91% (-35%/año) | -0.58% (-24%/año) |

## ARB ETH 0.05
Precio 1,660.93 (-4.0% desde el inicio) · mitad/mitad sin LP: -2.02%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 44.52 $ | -1.67% (-55%/año) | -1.84% (-58%/año) |
| ±5% | tras 24 h | 84% | 0 | 34.10 $ | +0.49% (+26%/año) | -2.22% (-66%/año) |
| ±10% | al salir | 100% | 0 | 26.19 $ | +0.12% (+6%/año) | -1.14% (-42%/año) |
| ±10% | tras 24 h | 100% | 0 | 26.19 $ | +0.12% (+6%/año) | -1.14% (-42%/año) |
| ±20% | al salir | 100% | 0 | 14.04 $ | -0.89% (-35%/año) | -0.56% (-23%/año) |
| ±20% | tras 24 h | 100% | 0 | 14.04 $ | -0.89% (-35%/año) | -0.56% (-23%/año) |

## ARB BTC 0.05
Precio 59,987.33 (-2.3% desde el inicio) · mitad/mitad sin LP: -1.16%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 28.53 $ | -1.63% (-54%/año) | -1.46% (-50%/año) |
| ±5% | tras 24 h | 87% | 0 | 23.46 $ | +0.86% (+50%/año) | -1.52% (-52%/año) |
| ±10% | al salir | 100% | 0 | 16.10 $ | +0.26% (+13%/año) | -0.70% (-28%/año) |
| ±10% | tras 24 h | 100% | 0 | 16.10 $ | +0.26% (+13%/año) | -0.70% (-28%/año) |
| ±20% | al salir | 100% | 0 | 8.61 $ | -0.42% (-18%/año) | -0.23% (-11%/año) |
| ±20% | tras 24 h | 100% | 0 | 8.61 $ | -0.42% (-18%/año) | -0.23% (-11%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
