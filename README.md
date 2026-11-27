# Prueba en vivo de LP concentrado

**Actualizado:** 27/11/2026 15:30 UTC · **7.1 días de datos** · 24 lecturas · huecos: 88

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,662.25 (-4.0% desde el inicio) · mitad/mitad sin LP: -1.99%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 95% | 2 | 45.12 $ | -1.89% (-62%/año) | -1.71% (-59%/año) |
| ±5% | tras 24 h | 83% | 0 | 32.52 $ | +0.28% (+15%/año) | -2.21% (-68%/año) |
| ±10% | al salir | 100% | 0 | 26.31 $ | +0.05% (+3%/año) | -0.97% (-39%/año) |
| ±10% | tras 24 h | 100% | 0 | 26.31 $ | +0.05% (+3%/año) | -0.97% (-39%/año) |
| ±20% | al salir | 100% | 0 | 14.53 $ | -0.94% (-38%/año) | -0.59% (-26%/año) |
| ±20% | tras 24 h | 100% | 0 | 14.53 $ | -0.94% (-38%/año) | -0.59% (-26%/año) |

## BASE ETH 0.05
Precio 1,662.27 (-4.0% desde el inicio) · mitad/mitad sin LP: -1.98%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 95% | 2 | 42.37 $ | -1.81% (-61%/año) | -2.03% (-65%/año) |
| ±5% | tras 24 h | 83% | 0 | 31.48 $ | +0.31% (+17%/año) | -2.47% (-72%/año) |
| ±10% | al salir | 100% | 0 | 25.09 $ | +0.07% (+4%/año) | -1.24% (-47%/año) |
| ±10% | tras 24 h | 100% | 0 | 25.09 $ | +0.07% (+4%/año) | -1.24% (-47%/año) |
| ±20% | al salir | 100% | 0 | 13.45 $ | -0.90% (-37%/año) | -0.62% (-27%/año) |
| ±20% | tras 24 h | 100% | 0 | 13.45 $ | -0.90% (-37%/año) | -0.62% (-27%/año) |

## ARB ETH 0.05
Precio 1,662.31 (-4.0% desde el inicio) · mitad/mitad sin LP: -1.98%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 95% | 2 | 43.25 $ | -1.75% (-59%/año) | -1.97% (-64%/año) |
| ±5% | tras 24 h | 83% | 0 | 32.81 $ | +0.44% (+25%/año) | -2.36% (-70%/año) |
| ±10% | al salir | 100% | 0 | 25.51 $ | +0.11% (+6%/año) | -1.21% (-46%/año) |
| ±10% | tras 24 h | 100% | 0 | 25.51 $ | +0.11% (+6%/año) | -1.21% (-46%/año) |
| ±20% | al salir | 100% | 0 | 13.68 $ | -0.88% (-36%/año) | -0.60% (-27%/año) |
| ±20% | tras 24 h | 100% | 0 | 13.68 $ | -0.88% (-36%/año) | -0.60% (-27%/año) |

## ARB BTC 0.05
Precio 59,836.22 (-2.6% desde el inicio) · mitad/mitad sin LP: -1.29%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 2 | 27.72 $ | -1.91% (-63%/año) | -1.54% (-55%/año) |
| ±5% | tras 24 h | 86% | 0 | 22.64 $ | +0.59% (+35%/año) | -1.60% (-56%/año) |
| ±10% | al salir | 100% | 0 | 15.67 $ | +0.06% (+3%/año) | -0.74% (-32%/año) |
| ±10% | tras 24 h | 100% | 0 | 15.67 $ | +0.06% (+3%/año) | -0.74% (-32%/año) |
| ±20% | al salir | 100% | 0 | 8.38 $ | -0.59% (-26%/año) | -0.26% (-12%/año) |
| ±20% | tras 24 h | 100% | 0 | 8.38 $ | -0.59% (-26%/año) | -0.26% (-12%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
