# Prueba en vivo de LP concentrado

**Actualizado:** 27/11/2026 23:42 UTC · **7.5 días de datos** · 25 lecturas · huecos: 92

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,658.23 (-4.2% desde el inicio) · mitad/mitad sin LP: -2.11%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 46.06 $ | -1.95% (-62%/año) | -1.61% (-55%/año) |
| ±5% | tras 24 h | 83% | 0 | 33.49 $ | +0.16% (+8%/año) | -2.11% (-65%/año) |
| ±10% | al salir | 100% | 0 | 26.81 $ | -0.07% (-3%/año) | -0.91% (-36%/año) |
| ±10% | tras 24 h | 100% | 0 | 26.81 $ | -0.07% (-3%/año) | -0.91% (-36%/año) |
| ±20% | al salir | 100% | 0 | 14.81 $ | -1.05% (-40%/año) | -0.56% (-24%/año) |
| ±20% | tras 24 h | 100% | 0 | 14.81 $ | -1.05% (-40%/año) | -0.56% (-24%/año) |

## BASE ETH 0.05
Precio 1,658.76 (-4.2% desde el inicio) · mitad/mitad sin LP: -2.08%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 43.41 $ | -1.84% (-60%/año) | -1.92% (-61%/año) |
| ±5% | tras 24 h | 83% | 0 | 32.53 $ | +0.22% (+12%/año) | -2.36% (-69%/año) |
| ±10% | al salir | 100% | 0 | 25.64 $ | -0.02% (-1%/año) | -1.18% (-44%/año) |
| ±10% | tras 24 h | 100% | 0 | 25.64 $ | -0.02% (-1%/año) | -1.18% (-44%/año) |
| ±20% | al salir | 100% | 0 | 13.74 $ | -0.99% (-39%/año) | -0.58% (-25%/año) |
| ±20% | tras 24 h | 100% | 0 | 13.74 $ | -0.99% (-39%/año) | -0.58% (-25%/año) |

## ARB ETH 0.05
Precio 1,658.71 (-4.2% desde el inicio) · mitad/mitad sin LP: -2.08%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 44.36 $ | -1.76% (-58%/año) | -1.85% (-60%/año) |
| ±5% | tras 24 h | 83% | 0 | 33.94 $ | +0.36% (+19%/año) | -2.24% (-67%/año) |
| ±10% | al salir | 100% | 0 | 26.10 $ | +0.02% (+1%/año) | -1.14% (-43%/año) |
| ±10% | tras 24 h | 100% | 0 | 26.10 $ | +0.02% (+1%/año) | -1.14% (-43%/año) |
| ±20% | al salir | 100% | 0 | 13.99 $ | -0.98% (-38%/año) | -0.56% (-24%/año) |
| ±20% | tras 24 h | 100% | 0 | 13.99 $ | -0.98% (-38%/año) | -0.56% (-24%/año) |

## ARB BTC 0.05
Precio 59,858.62 (-2.5% desde el inicio) · mitad/mitad sin LP: -1.27%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 28.42 $ | -1.81% (-59%/año) | -1.46% (-51%/año) |
| ±5% | tras 24 h | 87% | 0 | 23.34 $ | +0.69% (+40%/año) | -1.53% (-53%/año) |
| ±10% | al salir | 100% | 0 | 16.04 $ | +0.12% (+6%/año) | -0.70% (-29%/año) |
| ±10% | tras 24 h | 100% | 0 | 16.04 $ | +0.12% (+6%/año) | -0.70% (-29%/año) |
| ±20% | al salir | 100% | 0 | 8.58 $ | -0.55% (-24%/año) | -0.24% (-11%/año) |
| ±20% | tras 24 h | 100% | 0 | 8.58 $ | -0.55% (-24%/año) | -0.24% (-11%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
