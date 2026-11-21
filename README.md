# Prueba en vivo de LP concentrado

**Actualizado:** 21/11/2026 01:43 UTC · **0.6 días de datos** · 4 lecturas · huecos: 8

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,620.61 (-6.4% desde el inicio) · mitad/mitad sin LP: -3.19%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 69% | 1 | 4.83 $ | -5.64% | -2.46% |
| ±5% | tras 24 h | 31% | 0 | 3.55 $ | -5.00% | -2.39% |
| ±10% | al salir | 100% | 0 | 4.39 $ | -4.02% | -1.31% |
| ±10% | tras 24 h | 100% | 0 | 4.39 $ | -4.02% | -1.31% |
| ±20% | al salir | 100% | 0 | 2.42 $ | -3.72% | -0.81% |
| ±20% | tras 24 h | 100% | 0 | 2.42 $ | -3.72% | -0.81% |

## BASE ETH 0.05
Precio 1,619.38 (-6.4% desde el inicio) · mitad/mitad sin LP: -3.22%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 69% | 1 | 5.18 $ | -5.53% | -2.35% |
| ±5% | tras 24 h | 31% | 0 | 3.61 $ | -4.95% | -2.40% |
| ±10% | al salir | 100% | 0 | 4.61 $ | -3.93% | -1.31% |
| ±10% | tras 24 h | 100% | 0 | 4.61 $ | -3.93% | -1.31% |
| ±20% | al salir | 100% | 0 | 2.47 $ | -3.61% | -0.73% |
| ±20% | tras 24 h | 100% | 0 | 2.47 $ | -3.61% | -0.73% |

## ARB ETH 0.05
Precio 1,619.35 (-6.4% desde el inicio) · mitad/mitad sin LP: -3.22%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 69% | 1 | 4.79 $ | -5.59% | -2.41% |
| ±5% | tras 24 h | 31% | 0 | 3.47 $ | -4.97% | -2.43% |
| ±10% | al salir | 100% | 0 | 4.32 $ | -3.96% | -1.35% |
| ±10% | tras 24 h | 100% | 0 | 4.32 $ | -3.96% | -1.35% |
| ±20% | al salir | 100% | 0 | 2.32 $ | -3.64% | -0.76% |
| ±20% | tras 24 h | 100% | 0 | 2.32 $ | -3.64% | -0.76% |

## ARB BTC 0.05
Precio 58,969.98 (-4.0% desde el inicio) · mitad/mitad sin LP: -1.99%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 69% | 1 | 2.52 $ | -3.09% | -1.13% |
| ±5% | tras 24 h | 50% | 0 | 2.18 $ | -2.64% | -1.14% |
| ±10% | al salir | 100% | 0 | 2.28 $ | -2.24% | -0.51% |
| ±10% | tras 24 h | 100% | 0 | 2.28 $ | -2.24% | -0.51% |
| ±20% | al salir | 100% | 0 | 1.22 $ | -2.14% | -0.30% |
| ±20% | tras 24 h | 100% | 0 | 1.22 $ | -2.14% | -0.30% |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
