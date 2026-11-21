# Prueba en vivo de LP concentrado

**Actualizado:** 21/11/2026 16:34 UTC · **1.2 días de datos** · 6 lecturas · huecos: 16

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,678.62 (-3.0% desde el inicio) · mitad/mitad sin LP: -1.52%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 85% | 1 | 15.86 $ | -3.81% (-100%/año) | -1.83% (-100%/año) |
| ±5% | tras 24 h | 28% | 0 | 4.95 $ | -1.66% (-99%/año) | -2.45% (-100%/año) |
| ±10% | al salir | 100% | 0 | 10.27 $ | -0.90% (-94%/año) | -1.05% (-96%/año) |
| ±10% | tras 24 h | 100% | 0 | 10.27 $ | -0.90% (-94%/año) | -1.05% (-96%/año) |
| ±20% | al salir | 100% | 0 | 5.67 $ | -1.25% (-98%/año) | -0.64% (-86%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.67 $ | -1.25% (-98%/año) | -0.64% (-86%/año) |

## BASE ETH 0.05
Precio 1,680.98 (-2.9% desde el inicio) · mitad/mitad sin LP: -1.44%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 72% | 2 | 13.34 $ | -4.12% (-100%/año) | -2.05% (-100%/año) |
| ±5% | tras 24 h | 28% | 0 | 4.99 $ | -1.41% (-99%/año) | -2.48% (-100%/año) |
| ±10% | al salir | 100% | 0 | 9.68 $ | -0.73% (-89%/año) | -1.18% (-97%/año) |
| ±10% | tras 24 h | 100% | 0 | 9.68 $ | -0.73% (-89%/año) | -1.18% (-97%/año) |
| ±20% | al salir | 100% | 0 | 5.19 $ | -1.07% (-96%/año) | -0.66% (-87%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.19 $ | -1.07% (-96%/año) | -0.66% (-87%/año) |

## ARB ETH 0.05
Precio 1,680.94 (-2.9% desde el inicio) · mitad/mitad sin LP: -1.44%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 72% | 2 | 12.63 $ | -4.22% (-100%/año) | -2.14% (-100%/año) |
| ±5% | tras 24 h | 28% | 0 | 4.89 $ | -1.43% (-99%/año) | -2.50% (-100%/año) |
| ±10% | al salir | 100% | 0 | 9.25 $ | -0.78% (-91%/año) | -1.23% (-98%/año) |
| ±10% | tras 24 h | 100% | 0 | 9.25 $ | -0.78% (-91%/año) | -1.23% (-98%/año) |
| ±20% | al salir | 100% | 0 | 4.96 $ | -1.10% (-97%/año) | -0.70% (-88%/año) |
| ±20% | tras 24 h | 100% | 0 | 4.96 $ | -1.10% (-97%/año) | -0.70% (-88%/año) |

## ARB BTC 0.05
Precio 60,016.59 (-2.3% desde el inicio) · mitad/mitad sin LP: -1.14%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 85% | 1 | 8.14 $ | -1.98% (-100%/año) | -1.26% (-98%/año) |
| ±5% | tras 24 h | 50% | 0 | 4.99 $ | -0.95% (-95%/año) | -1.33% (-98%/año) |
| ±10% | al salir | 100% | 0 | 5.23 $ | -0.80% (-92%/año) | -0.58% (-84%/año) |
| ±10% | tras 24 h | 100% | 0 | 5.23 $ | -0.80% (-92%/año) | -0.58% (-84%/año) |
| ±20% | al salir | 100% | 0 | 2.80 $ | -0.98% (-95%/año) | -0.24% (-53%/año) |
| ±20% | tras 24 h | 100% | 0 | 2.80 $ | -0.98% (-95%/año) | -0.24% (-53%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
