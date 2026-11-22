# Prueba en vivo de LP concentrado

**Actualizado:** 22/11/2026 09:33 UTC · **1.9 días de datos** · 9 lecturas · huecos: 28

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,687.45 (-2.5% desde el inicio) · mitad/mitad sin LP: -1.26%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 82% | 2 | 16.80 $ | -3.87% (-100%/año) | -1.93% (-98%/año) |
| ±5% | tras 24 h | 55% | 0 | 6.67 $ | -1.09% (-88%/año) | -2.30% (-99%/año) |
| ±10% | al salir | 100% | 0 | 11.17 $ | -0.48% (-61%/año) | -0.97% (-85%/año) |
| ±10% | tras 24 h | 100% | 0 | 11.17 $ | -0.48% (-61%/año) | -0.97% (-85%/año) |
| ±20% | al salir | 100% | 0 | 6.17 $ | -0.91% (-83%/año) | -0.60% (-69%/año) |
| ±20% | tras 24 h | 100% | 0 | 6.17 $ | -0.91% (-83%/año) | -0.60% (-69%/año) |

## BASE ETH 0.05
Precio 1,686.94 (-2.5% desde el inicio) · mitad/mitad sin LP: -1.26%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 82% | 2 | 15.14 $ | -3.78% (-100%/año) | -1.88% (-97%/año) |
| ±5% | tras 24 h | 55% | 0 | 6.83 $ | -0.96% (-84%/año) | -2.30% (-99%/año) |
| ±10% | al salir | 100% | 0 | 10.64 $ | -0.41% (-55%/año) | -1.09% (-88%/año) |
| ±10% | tras 24 h | 100% | 0 | 10.64 $ | -0.41% (-55%/año) | -1.09% (-88%/año) |
| ±20% | al salir | 100% | 0 | 5.70 $ | -0.82% (-80%/año) | -0.62% (-70%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.70 $ | -0.82% (-80%/año) | -0.62% (-70%/año) |

## ARB ETH 0.05
Precio 1,687.04 (-2.5% desde el inicio) · mitad/mitad sin LP: -1.26%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 82% | 2 | 14.49 $ | -3.86% (-100%/año) | -1.97% (-98%/año) |
| ±5% | tras 24 h | 55% | 0 | 6.79 $ | -0.96% (-85%/año) | -2.32% (-99%/año) |
| ±10% | al salir | 100% | 0 | 10.24 $ | -0.45% (-58%/año) | -1.14% (-89%/año) |
| ±10% | tras 24 h | 100% | 0 | 10.24 $ | -0.45% (-58%/año) | -1.14% (-89%/año) |
| ±20% | al salir | 100% | 0 | 5.49 $ | -0.85% (-81%/año) | -0.65% (-72%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.49 $ | -0.85% (-81%/año) | -0.65% (-72%/año) |

## ARB BTC 0.05
Precio 60,019.10 (-2.3% desde el inicio) · mitad/mitad sin LP: -1.14%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 91% | 1 | 9.46 $ | -1.84% (-97%/año) | -1.17% (-90%/año) |
| ±5% | tras 24 h | 69% | 0 | 6.32 $ | -0.82% (-79%/año) | -1.24% (-91%/año) |
| ±10% | al salir | 100% | 0 | 5.93 $ | -0.73% (-76%/año) | -0.54% (-65%/año) |
| ±10% | tras 24 h | 100% | 0 | 5.93 $ | -0.73% (-76%/año) | -0.54% (-65%/año) |
| ±20% | al salir | 100% | 0 | 3.17 $ | -0.94% (-84%/año) | -0.20% (-32%/año) |
| ±20% | tras 24 h | 100% | 0 | 3.17 $ | -0.94% (-84%/año) | -0.20% (-32%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
