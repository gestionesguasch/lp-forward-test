# Prueba en vivo de LP concentrado

**Actualizado:** 25/11/2026 03:54 UTC · **4.7 días de datos** · 17 lecturas · huecos: 60

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,664.03 (-3.9% desde el inicio) · mitad/mitad sin LP: -1.94%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 93% | 2 | 32.22 $ | -3.11% (-92%/año) | -0.67% (-41%/año) |
| ±5% | tras 24 h | 82% | 0 | 22.48 $ | -0.63% (-39%/año) | -1.00% (-55%/año) |
| ±10% | al salir | 100% | 0 | 19.41 $ | -0.57% (-36%/año) | -0.37% (-25%/año) |
| ±10% | tras 24 h | 100% | 0 | 19.41 $ | -0.57% (-36%/año) | -0.37% (-25%/año) |
| ±20% | al salir | 100% | 0 | 10.72 $ | -1.25% (-63%/año) | -0.29% (-20%/año) |
| ±20% | tras 24 h | 100% | 0 | 10.72 $ | -1.25% (-63%/año) | -0.29% (-20%/año) |

## BASE ETH 0.05
Precio 1,660.54 (-4.1% desde el inicio) · mitad/mitad sin LP: -2.03%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 93% | 2 | 30.08 $ | -3.10% (-92%/año) | -0.72% (-43%/año) |
| ±5% | tras 24 h | 82% | 0 | 22.03 $ | -0.73% (-44%/año) | -1.19% (-61%/año) |
| ±10% | al salir | 100% | 0 | 18.57 $ | -0.65% (-40%/año) | -0.54% (-34%/año) |
| ±10% | tras 24 h | 100% | 0 | 18.57 $ | -0.65% (-40%/año) | -0.54% (-34%/año) |
| ±20% | al salir | 100% | 0 | 9.95 $ | -1.31% (-64%/año) | -0.33% (-23%/año) |
| ±20% | tras 24 h | 100% | 0 | 9.95 $ | -1.31% (-64%/año) | -0.33% (-23%/año) |

## ARB ETH 0.05
Precio 1,660.54 (-4.1% desde el inicio) · mitad/mitad sin LP: -2.03%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 93% | 2 | 30.39 $ | -3.09% (-92%/año) | -0.71% (-43%/año) |
| ±5% | tras 24 h | 82% | 0 | 22.97 $ | -0.64% (-40%/año) | -1.11% (-58%/año) |
| ±10% | al salir | 100% | 0 | 18.69 $ | -0.65% (-40%/año) | -0.54% (-34%/año) |
| ±10% | tras 24 h | 100% | 0 | 18.69 $ | -0.65% (-40%/año) | -0.54% (-34%/año) |
| ±20% | al salir | 100% | 0 | 10.02 $ | -1.31% (-64%/año) | -0.33% (-23%/año) |
| ±20% | tras 24 h | 100% | 0 | 10.02 $ | -1.31% (-64%/año) | -0.33% (-23%/año) |

## ARB BTC 0.05
Precio 59,400.27 (-3.3% desde el inicio) · mitad/mitad sin LP: -1.64%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 1 | 19.47 $ | -1.13% (-59%/año) | -0.59% (-37%/año) |
| ±5% | tras 24 h | 87% | 0 | 16.33 $ | -0.61% (-38%/año) | -0.68% (-41%/año) |
| ±10% | al salir | 100% | 0 | 11.17 $ | -0.86% (-49%/año) | -0.28% (-19%/año) |
| ±10% | tras 24 h | 100% | 0 | 11.17 $ | -0.86% (-49%/año) | -0.28% (-19%/año) |
| ±20% | al salir | 100% | 0 | 5.97 $ | -1.24% (-63%/año) | -0.00% (-0%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.97 $ | -1.24% (-63%/año) | -0.00% (-0%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
