# Prueba en vivo de LP concentrado

**Actualizado:** 22/11/2026 01:55 UTC · **1.6 días de datos** · 8 lecturas · huecos: 24

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,681.52 (-2.9% desde el inicio) · mitad/mitad sin LP: -1.44%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 89% | 1 | 16.06 $ | -3.79% (-100%/año) | -1.82% (-99%/año) |
| ±5% | tras 24 h | 46% | 0 | 5.16 $ | -1.51% (-97%/año) | -2.43% (-100%/año) |
| ±10% | al salir | 100% | 0 | 10.38 $ | -0.78% (-84%/año) | -1.04% (-91%/año) |
| ±10% | tras 24 h | 100% | 0 | 10.38 $ | -0.78% (-84%/año) | -1.04% (-91%/año) |
| ±20% | al salir | 100% | 0 | 5.73 $ | -1.15% (-93%/año) | -0.64% (-77%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.73 $ | -1.15% (-93%/año) | -0.64% (-77%/año) |

## BASE ETH 0.05
Precio 1,684.82 (-2.6% desde el inicio) · mitad/mitad sin LP: -1.32%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 79% | 2 | 13.86 $ | -3.96% (-100%/año) | -2.00% (-99%/año) |
| ±5% | tras 24 h | 46% | 0 | 5.53 $ | -1.18% (-94%/año) | -2.43% (-100%/año) |
| ±10% | al salir | 100% | 0 | 9.96 $ | -0.55% (-73%/año) | -1.15% (-93%/año) |
| ±10% | tras 24 h | 100% | 0 | 9.96 $ | -0.55% (-73%/año) | -1.15% (-93%/año) |
| ±20% | al salir | 100% | 0 | 5.34 $ | -0.93% (-89%/año) | -0.65% (-78%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.34 $ | -0.93% (-89%/año) | -0.65% (-78%/año) |

## ARB ETH 0.05
Precio 1,684.81 (-2.7% desde el inicio) · mitad/mitad sin LP: -1.33%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 79% | 2 | 13.21 $ | -4.05% (-100%/año) | -2.09% (-99%/año) |
| ±5% | tras 24 h | 46% | 0 | 5.48 $ | -1.19% (-94%/año) | -2.45% (-100%/año) |
| ±10% | al salir | 100% | 0 | 9.56 $ | -0.60% (-75%/año) | -1.21% (-94%/año) |
| ±10% | tras 24 h | 100% | 0 | 9.56 $ | -0.60% (-75%/año) | -1.21% (-94%/año) |
| ±20% | al salir | 100% | 0 | 5.13 $ | -0.96% (-89%/año) | -0.68% (-80%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.13 $ | -0.96% (-89%/año) | -0.68% (-80%/año) |

## ARB BTC 0.05
Precio 60,177.73 (-2.0% desde el inicio) · mitad/mitad sin LP: -1.01%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 89% | 1 | 8.65 $ | -1.87% (-99%/año) | -1.25% (-95%/año) |
| ±5% | tras 24 h | 62% | 0 | 5.50 $ | -0.71% (-81%/año) | -1.33% (-96%/año) |
| ±10% | al salir | 100% | 0 | 5.50 $ | -0.61% (-76%/año) | -0.58% (-74%/año) |
| ±10% | tras 24 h | 100% | 0 | 5.50 $ | -0.61% (-76%/año) | -0.58% (-74%/año) |
| ±20% | al salir | 100% | 0 | 2.94 $ | -0.82% (-85%/año) | -0.23% (-42%/año) |
| ±20% | tras 24 h | 100% | 0 | 2.94 $ | -0.82% (-85%/año) | -0.23% (-42%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
