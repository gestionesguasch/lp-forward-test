# Prueba en vivo de LP concentrado

**Actualizado:** 21/11/2026 21:52 UTC · **1.4 días de datos** · 7 lecturas · huecos: 20

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,681.97 (-2.8% desde el inicio) · mitad/mitad sin LP: -1.42%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 88% | 1 | 15.93 $ | -3.80% (-100%/año) | -1.83% (-99%/año) |
| ±5% | tras 24 h | 40% | 0 | 5.03 $ | -1.50% (-98%/año) | -2.45% (-100%/año) |
| ±10% | al salir | 100% | 0 | 10.31 $ | -0.77% (-87%/año) | -1.05% (-94%/año) |
| ±10% | tras 24 h | 100% | 0 | 10.31 $ | -0.77% (-87%/año) | -1.05% (-94%/año) |
| ±20% | al salir | 100% | 0 | 5.70 $ | -1.14% (-95%/año) | -0.64% (-81%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.70 $ | -1.14% (-95%/año) | -0.64% (-81%/año) |

## BASE ETH 0.05
Precio 1,684.99 (-2.6% desde el inicio) · mitad/mitad sin LP: -1.32%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 76% | 2 | 13.69 $ | -3.98% (-100%/año) | -2.02% (-100%/año) |
| ±5% | tras 24 h | 40% | 0 | 5.36 $ | -1.19% (-96%/año) | -2.45% (-100%/año) |
| ±10% | al salir | 100% | 0 | 9.87 $ | -0.56% (-77%/año) | -1.16% (-95%/año) |
| ±10% | tras 24 h | 100% | 0 | 9.87 $ | -0.56% (-77%/año) | -1.16% (-95%/año) |
| ±20% | al salir | 100% | 0 | 5.29 $ | -0.93% (-91%/año) | -0.66% (-82%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.29 $ | -0.93% (-91%/año) | -0.66% (-82%/año) |

## ARB ETH 0.05
Precio 1,684.58 (-2.7% desde el inicio) · mitad/mitad sin LP: -1.33%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 76% | 2 | 13.00 $ | -4.08% (-100%/año) | -2.11% (-100%/año) |
| ±5% | tras 24 h | 40% | 0 | 5.27 $ | -1.23% (-96%/año) | -2.47% (-100%/año) |
| ±10% | al salir | 100% | 0 | 9.45 $ | -0.62% (-80%/año) | -1.22% (-96%/año) |
| ±10% | tras 24 h | 100% | 0 | 9.45 $ | -0.62% (-80%/año) | -1.22% (-96%/año) |
| ±20% | al salir | 100% | 0 | 5.07 $ | -0.97% (-92%/año) | -0.69% (-84%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.07 $ | -0.97% (-92%/año) | -0.69% (-84%/año) |

## ARB BTC 0.05
Precio 60,454.17 (-1.6% desde el inicio) · mitad/mitad sin LP: -0.78%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 88% | 1 | 8.50 $ | -1.80% (-99%/año) | -1.25% (-96%/año) |
| ±5% | tras 24 h | 58% | 0 | 5.35 $ | -0.42% (-66%/año) | -1.33% (-97%/año) |
| ±10% | al salir | 100% | 0 | 5.42 $ | -0.35% (-60%/año) | -0.58% (-78%/año) |
| ±10% | tras 24 h | 100% | 0 | 5.42 $ | -0.35% (-60%/año) | -0.58% (-78%/año) |
| ±20% | al salir | 100% | 0 | 2.90 $ | -0.57% (-78%/año) | -0.24% (-47%/año) |
| ±20% | tras 24 h | 100% | 0 | 2.90 $ | -0.57% (-78%/año) | -0.24% (-47%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
