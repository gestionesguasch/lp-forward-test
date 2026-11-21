# Prueba en vivo de LP concentrado

**Actualizado:** 21/11/2026 08:51 UTC · **0.9 días de datos** · 5 lecturas · huecos: 12

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,627.75 (-6.0% desde el inicio) · mitad/mitad sin LP: -2.99%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 80% | 1 | 13.11 $ | -4.66% | -1.64% |
| ±5% | tras 24 h | 20% | 0 | 3.55 $ | -4.59% | -2.39% |
| ±10% | al salir | 100% | 0 | 8.81 $ | -3.23% | -0.87% |
| ±10% | tras 24 h | 100% | 0 | 8.81 $ | -3.23% | -0.87% |
| ±20% | al salir | 100% | 0 | 4.86 $ | -3.19% | -0.58% |
| ±20% | tras 24 h | 100% | 0 | 4.86 $ | -3.19% | -0.58% |

## BASE ETH 0.05
Precio 1,631.20 (-5.7% desde el inicio) · mitad/mitad sin LP: -2.87%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 80% | 1 | 11.99 $ | -4.63% | -1.69% |
| ±5% | tras 24 h | 20% | 0 | 3.61 $ | -4.26% | -2.40% |
| ±10% | al salir | 100% | 0 | 8.24 $ | -2.99% | -0.96% |
| ±10% | tras 24 h | 100% | 0 | 8.24 $ | -2.99% | -0.96% |
| ±20% | al salir | 100% | 0 | 4.42 $ | -2.95% | -0.54% |
| ±20% | tras 24 h | 100% | 0 | 4.42 $ | -2.95% | -0.54% |

## ARB ETH 0.05
Precio 1,631.28 (-5.7% desde el inicio) · mitad/mitad sin LP: -2.87%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 80% | 1 | 11.25 $ | -4.72% | -1.79% |
| ±5% | tras 24 h | 20% | 0 | 3.47 $ | -4.27% | -2.42% |
| ±10% | al salir | 100% | 0 | 7.78 $ | -3.04% | -1.02% |
| ±10% | tras 24 h | 100% | 0 | 7.78 $ | -3.04% | -1.02% |
| ±20% | al salir | 100% | 0 | 4.17 $ | -2.98% | -0.58% |
| ±20% | tras 24 h | 100% | 0 | 4.17 $ | -2.98% | -0.58% |

## ARB BTC 0.05
Precio 58,068.75 (-5.4% desde el inicio) · mitad/mitad sin LP: -2.72%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 80% | 1 | 6.20 $ | -3.44% | -0.89% |
| ±5% | tras 24 h | 50% | 0 | 4.02 $ | -3.90% | -1.06% |
| ±10% | al salir | 100% | 0 | 4.21 $ | -3.16% | -0.39% |
| ±10% | tras 24 h | 100% | 0 | 4.21 $ | -3.16% | -0.39% |
| ±20% | al salir | 100% | 0 | 2.25 $ | -2.98% | -0.20% |
| ±20% | tras 24 h | 100% | 0 | 2.25 $ | -2.98% | -0.20% |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
