# Prueba en vivo de LP concentrado

**Actualizado:** 26/11/2026 14:58 UTC · **6.1 días de datos** · 21 lecturas · huecos: 76

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,700.11 (-1.8% desde el inicio) · mitad/mitad sin LP: -0.90%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 95% | 2 | 40.22 $ | -1.18% (-51%/año) | -0.59% (-30%/año) |
| ±5% | tras 24 h | 80% | 0 | 27.50 $ | +1.52% (+146%/año) | -1.06% (-47%/año) |
| ±10% | al salir | 100% | 0 | 23.69 $ | +1.22% (+106%/año) | -0.38% (-20%/año) |
| ±10% | tras 24 h | 100% | 0 | 23.69 $ | +1.22% (+106%/año) | -0.38% (-20%/año) |
| ±20% | al salir | 100% | 0 | 13.08 $ | +0.20% (+12%/año) | -0.27% (-15%/año) |
| ±20% | tras 24 h | 100% | 0 | 13.08 $ | +0.20% (+12%/año) | -0.27% (-15%/año) |

## BASE ETH 0.05
Precio 1,697.01 (-1.9% desde el inicio) · mitad/mitad sin LP: -0.97%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 95% | 2 | 37.79 $ | -1.27% (-53%/año) | -0.70% (-34%/año) |
| ±5% | tras 24 h | 80% | 0 | 26.81 $ | +1.47% (+139%/año) | -1.12% (-49%/año) |
| ±10% | al salir | 100% | 0 | 22.66 $ | +1.15% (+98%/año) | -0.53% (-27%/año) |
| ±10% | tras 24 h | 100% | 0 | 22.66 $ | +1.15% (+98%/año) | -0.53% (-27%/año) |
| ±20% | al salir | 100% | 0 | 12.14 $ | +0.15% (+9%/año) | -0.33% (-18%/año) |
| ±20% | tras 24 h | 100% | 0 | 12.14 $ | +0.15% (+9%/año) | -0.33% (-18%/año) |

## ARB ETH 0.05
Precio 1,697.02 (-1.9% desde el inicio) · mitad/mitad sin LP: -0.97%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 95% | 2 | 38.66 $ | -1.20% (-51%/año) | -0.63% (-32%/año) |
| ±5% | tras 24 h | 80% | 0 | 28.13 $ | +1.59% (+157%/año) | -1.00% (-45%/año) |
| ±10% | al salir | 100% | 0 | 23.08 $ | +1.19% (+103%/año) | -0.50% (-26%/año) |
| ±10% | tras 24 h | 100% | 0 | 23.08 $ | +1.19% (+103%/año) | -0.50% (-26%/año) |
| ±20% | al salir | 100% | 0 | 12.37 $ | +0.17% (+10%/año) | -0.31% (-17%/año) |
| ±20% | tras 24 h | 100% | 0 | 12.37 $ | +0.17% (+10%/año) | -0.31% (-17%/año) |

## ARB BTC 0.05
Precio 60,831.56 (-1.0% desde el inicio) · mitad/mitad sin LP: -0.48%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 97% | 1 | 25.28 $ | -0.05% (-3%/año) | -0.95% (-43%/año) |
| ±5% | tras 24 h | 84% | 0 | 19.89 $ | +1.42% (+132%/año) | -1.06% (-47%/año) |
| ±10% | al salir | 100% | 0 | 14.23 $ | +0.88% (+69%/año) | -0.46% (-24%/año) |
| ±10% | tras 24 h | 100% | 0 | 14.23 $ | +0.88% (+69%/año) | -0.46% (-24%/año) |
| ±20% | al salir | 100% | 0 | 7.61 $ | +0.23% (+15%/año) | -0.16% (-9%/año) |
| ±20% | tras 24 h | 100% | 0 | 7.61 $ | +0.23% (+15%/año) | -0.16% (-9%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
