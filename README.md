# Prueba en vivo de LP concentrado

**Actualizado:** 20/11/2026 20:32 UTC · **0.3 días de datos** · 3 lecturas · huecos: 4

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,601.96 (-7.5% desde el inicio) · mitad/mitad sin LP: -3.73%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 50% | 1 | 3.55 $ | -6.25% | -2.52% |
| ±5% | tras 24 h | 50% | 0 | 3.55 $ | -6.09% | -2.38% |
| ±10% | al salir | 100% | 0 | 3.70 $ | -5.04% | -1.34% |
| ±10% | tras 24 h | 100% | 0 | 3.70 $ | -5.04% | -1.34% |
| ±20% | al salir | 100% | 0 | 2.04 $ | -4.52% | -0.82% |
| ±20% | tras 24 h | 100% | 0 | 2.04 $ | -4.52% | -0.82% |

## BASE ETH 0.05
Precio 1,598.06 (-7.7% desde el inicio) · mitad/mitad sin LP: -3.83%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 50% | 1 | 3.61 $ | -6.23% | -2.41% |
| ±5% | tras 24 h | 50% | 0 | 3.61 $ | -6.19% | -2.39% |
| ±10% | al salir | 100% | 0 | 3.77 $ | -5.11% | -1.34% |
| ±10% | tras 24 h | 100% | 0 | 3.77 $ | -5.11% | -1.34% |
| ±20% | al salir | 100% | 0 | 2.02 $ | -4.54% | -0.75% |
| ±20% | tras 24 h | 100% | 0 | 2.02 $ | -4.54% | -0.75% |

## ARB ETH 0.05
Precio 1,597.87 (-7.7% desde el inicio) · mitad/mitad sin LP: -3.84%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 50% | 1 | 3.47 $ | -6.27% | -2.44% |
| ±5% | tras 24 h | 50% | 0 | 3.47 $ | -6.22% | -2.42% |
| ±10% | al salir | 100% | 0 | 3.62 $ | -5.14% | -1.36% |
| ±10% | tras 24 h | 100% | 0 | 3.62 $ | -5.14% | -1.36% |
| ±20% | al salir | 100% | 0 | 1.94 $ | -4.56% | -0.76% |
| ±20% | tras 24 h | 100% | 0 | 1.94 $ | -4.56% | -0.76% |

## ARB BTC 0.05
Precio 58,442.05 (-4.8% desde el inicio) · mitad/mitad sin LP: -2.42%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 50% | 1 | 1.84 $ | -3.55% | -1.15% |
| ±5% | tras 24 h | 50% | 0 | 1.84 $ | -3.51% | -1.13% |
| ±10% | al salir | 100% | 0 | 1.92 $ | -2.91% | -0.53% |
| ±10% | tras 24 h | 100% | 0 | 1.92 $ | -2.91% | -0.53% |
| ±20% | al salir | 100% | 0 | 1.03 $ | -2.71% | -0.31% |
| ±20% | tras 24 h | 100% | 0 | 1.03 $ | -2.71% | -0.31% |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
