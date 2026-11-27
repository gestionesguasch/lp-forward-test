# Prueba en vivo de LP concentrado

**Actualizado:** 27/11/2026 05:26 UTC · **6.7 días de datos** · 23 lecturas · huecos: 84

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,742.34 (+0.6% desde el inicio) · mitad/mitad sin LP: +0.32%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 95% | 2 | 42.53 $ | -0.17% (-9%/año) | -0.90% (-39%/año) |
| ±5% | tras 24 h | 81% | 0 | 29.87 $ | +3.12% (+432%/año) | -1.38% (-53%/año) |
| ±10% | al salir | 100% | 0 | 24.92 $ | +2.64% (+312%/año) | -0.54% (-25%/año) |
| ±10% | tras 24 h | 100% | 0 | 24.92 $ | +2.64% (+312%/año) | -0.54% (-25%/año) |
| ±20% | al salir | 100% | 0 | 13.76 $ | +1.53% (+128%/año) | -0.35% (-18%/año) |
| ±20% | tras 24 h | 100% | 0 | 13.76 $ | +1.53% (+128%/año) | -0.35% (-18%/año) |

## BASE ETH 0.05
Precio 1,743.42 (+0.7% desde el inicio) · mitad/mitad sin LP: +0.37%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 95% | 2 | 39.92 $ | -0.36% (-18%/año) | -1.14% (-46%/año) |
| ±5% | tras 24 h | 81% | 0 | 28.98 $ | +3.20% (+454%/año) | -1.56% (-57%/año) |
| ±10% | al salir | 100% | 0 | 23.79 $ | +2.69% (+323%/año) | -0.76% (-34%/año) |
| ±10% | tras 24 h | 100% | 0 | 23.79 $ | +2.69% (+323%/año) | -0.76% (-34%/año) |
| ±20% | al salir | 100% | 0 | 12.75 $ | +1.60% (+136%/año) | -0.36% (-18%/año) |
| ±20% | tras 24 h | 100% | 0 | 12.75 $ | +1.60% (+136%/año) | -0.36% (-18%/año) |

## ARB ETH 0.05
Precio 1,743.49 (+0.7% desde el inicio) · mitad/mitad sin LP: +0.37%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 95% | 2 | 40.71 $ | -0.30% (-15%/año) | -1.08% (-45%/año) |
| ±5% | tras 24 h | 81% | 0 | 30.22 $ | +3.32% (+490%/año) | -1.46% (-55%/año) |
| ±10% | al salir | 100% | 0 | 24.17 $ | +2.72% (+331%/año) | -0.74% (-33%/año) |
| ±10% | tras 24 h | 100% | 0 | 24.17 $ | +2.72% (+331%/año) | -0.74% (-33%/año) |
| ±20% | al salir | 100% | 0 | 12.95 $ | +1.61% (+138%/año) | -0.35% (-17%/año) |
| ±20% | tras 24 h | 100% | 0 | 12.95 $ | +1.61% (+138%/año) | -0.35% (-17%/año) |

## ARB BTC 0.05
Precio 61,794.29 (+0.6% desde el inicio) · mitad/mitad sin LP: +0.31%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 26.17 $ | +0.04% (+2%/año) | -1.16% (-47%/año) |
| ±5% | tras 24 h | 85% | 0 | 21.09 $ | +2.35% (+254%/año) | -1.23% (-49%/año) |
| ±10% | al salir | 100% | 0 | 14.86 $ | +1.74% (+155%/año) | -0.55% (-26%/año) |
| ±10% | tras 24 h | 100% | 0 | 14.86 $ | +1.74% (+155%/año) | -0.55% (-26%/año) |
| ±20% | al salir | 100% | 0 | 7.94 $ | +1.05% (+77%/año) | -0.16% (-8%/año) |
| ±20% | tras 24 h | 100% | 0 | 7.94 $ | +1.05% (+77%/año) | -0.16% (-8%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
