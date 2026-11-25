# Prueba en vivo de LP concentrado

**Actualizado:** 25/11/2026 14:00 UTC · **5.1 días de datos** · 18 lecturas · huecos: 64

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,632.34 (-5.7% desde el inicio) · mitad/mitad sin LP: -2.86%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 93% | 2 | 33.89 $ | -4.31% (-96%/año) | -0.71% (-40%/año) |
| ±5% | tras 24 h | 79% | 0 | 23.34 $ | -2.34% (-82%/año) | -1.18% (-57%/año) |
| ±10% | al salir | 100% | 0 | 20.31 $ | -1.87% (-74%/año) | -0.44% (-27%/año) |
| ±10% | tras 24 h | 100% | 0 | 20.31 $ | -1.87% (-74%/año) | -0.44% (-27%/año) |
| ±20% | al salir | 100% | 0 | 11.22 $ | -2.38% (-82%/año) | -0.31% (-20%/año) |
| ±20% | tras 24 h | 100% | 0 | 11.22 $ | -2.38% (-82%/año) | -0.31% (-20%/año) |

## BASE ETH 0.05
Precio 1,628.88 (-5.9% desde el inicio) · mitad/mitad sin LP: -2.94%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 93% | 2 | 32.29 $ | -4.19% (-95%/año) | -0.70% (-40%/año) |
| ±5% | tras 24 h | 79% | 0 | 23.15 $ | -2.44% (-83%/año) | -1.23% (-59%/año) |
| ±10% | al salir | 100% | 0 | 19.74 $ | -1.95% (-76%/año) | -0.54% (-32%/año) |
| ±10% | tras 24 h | 100% | 0 | 19.74 $ | -1.95% (-76%/año) | -0.54% (-32%/año) |
| ±20% | al salir | 100% | 0 | 10.58 $ | -2.43% (-83%/año) | -0.34% (-21%/año) |
| ±20% | tras 24 h | 100% | 0 | 10.58 $ | -2.43% (-83%/año) | -0.34% (-21%/año) |

## ARB ETH 0.05
Precio 1,628.97 (-5.9% desde el inicio) · mitad/mitad sin LP: -2.94%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 93% | 2 | 32.66 $ | -4.17% (-95%/año) | -0.69% (-39%/año) |
| ±5% | tras 24 h | 79% | 0 | 24.13 $ | -2.34% (-82%/año) | -1.14% (-56%/año) |
| ±10% | al salir | 100% | 0 | 19.89 $ | -1.94% (-75%/año) | -0.54% (-32%/año) |
| ±10% | tras 24 h | 100% | 0 | 19.89 $ | -1.94% (-75%/año) | -0.54% (-32%/año) |
| ±20% | al salir | 100% | 0 | 10.66 $ | -2.42% (-83%/año) | -0.34% (-21%/año) |
| ±20% | tras 24 h | 100% | 0 | 10.66 $ | -2.42% (-83%/año) | -0.34% (-21%/año) |

## ARB BTC 0.05
Precio 58,112.01 (-5.4% desde el inicio) · mitad/mitad sin LP: -2.69%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 97% | 1 | 20.92 $ | -1.93% (-75%/año) | -0.70% (-40%/año) |
| ±5% | tras 24 h | 84% | 0 | 17.06 $ | -2.53% (-84%/año) | -0.85% (-46%/año) |
| ±10% | al salir | 100% | 0 | 11.94 $ | -2.33% (-82%/año) | -0.34% (-22%/año) |
| ±10% | tras 24 h | 100% | 0 | 11.94 $ | -2.33% (-82%/año) | -0.34% (-22%/año) |
| ±20% | al salir | 100% | 0 | 6.38 $ | -2.52% (-84%/año) | -0.10% (-7%/año) |
| ±20% | tras 24 h | 100% | 0 | 6.38 $ | -2.52% (-84%/año) | -0.10% (-7%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
