# Prueba en vivo de LP concentrado

**Actualizado:** 22/11/2026 22:41 UTC · **2.4 días de datos** · 11 lecturas · huecos: 36

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,714.05 (-1.0% desde el inicio) · mitad/mitad sin LP: -0.50%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 86% | 2 | 18.63 $ | -3.02% (-99%/año) | -1.87% (-94%/año) |
| ±5% | tras 24 h | 65% | 0 | 8.55 $ | +0.14% (+24%/año) | -2.24% (-97%/año) |
| ±10% | al salir | 100% | 0 | 12.15 $ | +0.53% (+120%/año) | -0.99% (-77%/año) |
| ±10% | tras 24 h | 100% | 0 | 12.15 $ | +0.53% (+120%/año) | -0.99% (-77%/año) |
| ±20% | al salir | 100% | 0 | 6.71 $ | -0.00% (-1%/año) | -0.61% (-60%/año) |
| ±20% | tras 24 h | 100% | 0 | 6.71 $ | -0.00% (-1%/año) | -0.61% (-60%/año) |

## BASE ETH 0.05
Precio 1,711.02 (-1.1% desde el inicio) · mitad/mitad sin LP: -0.57%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 86% | 2 | 16.92 $ | -3.07% (-99%/año) | -1.82% (-94%/año) |
| ±5% | tras 24 h | 65% | 0 | 8.64 $ | +0.19% (+32%/año) | -2.30% (-97%/año) |
| ±10% | al salir | 100% | 0 | 11.59 $ | +0.52% (+117%/año) | -1.09% (-81%/año) |
| ±10% | tras 24 h | 100% | 0 | 11.59 $ | +0.52% (+117%/año) | -1.09% (-81%/año) |
| ±20% | al salir | 100% | 0 | 6.21 $ | -0.00% (-1%/año) | -0.62% (-61%/año) |
| ±20% | tras 24 h | 100% | 0 | 6.21 $ | -0.00% (-1%/año) | -0.62% (-61%/año) |

## ARB ETH 0.05
Precio 1,710.78 (-1.2% desde el inicio) · mitad/mitad sin LP: -0.58%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 86% | 2 | 16.33 $ | -3.15% (-99%/año) | -1.90% (-94%/año) |
| ±5% | tras 24 h | 65% | 0 | 8.66 $ | +0.17% (+30%/año) | -2.31% (-97%/año) |
| ±10% | al salir | 100% | 0 | 11.22 $ | +0.47% (+101%/año) | -1.14% (-82%/año) |
| ±10% | tras 24 h | 100% | 0 | 11.22 $ | +0.47% (+101%/año) | -1.14% (-82%/año) |
| ±20% | al salir | 100% | 0 | 6.01 $ | -0.04% (-6%/año) | -0.65% (-62%/año) |
| ±20% | tras 24 h | 100% | 0 | 6.01 $ | -0.04% (-6%/año) | -0.65% (-62%/año) |

## ARB BTC 0.05
Precio 60,902.20 (-0.8% desde el inicio) · mitad/mitad sin LP: -0.42%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 93% | 1 | 10.72 $ | -1.49% (-90%/año) | -1.16% (-83%/año) |
| ±5% | tras 24 h | 76% | 0 | 7.57 $ | +0.26% (+47%/año) | -1.19% (-83%/año) |
| ±10% | al salir | 100% | 0 | 6.58 $ | +0.18% (+30%/año) | -0.54% (-55%/año) |
| ±10% | tras 24 h | 100% | 0 | 6.58 $ | +0.18% (+30%/año) | -0.54% (-55%/año) |
| ±20% | al salir | 100% | 0 | 3.52 $ | -0.12% (-17%/año) | -0.20% (-26%/año) |
| ±20% | tras 24 h | 100% | 0 | 3.52 $ | -0.12% (-17%/año) | -0.20% (-26%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
