# Prueba en vivo de LP concentrado

**Actualizado:** 23/11/2026 03:12 UTC · **2.6 días de datos** · 12 lecturas · huecos: 40

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,712.83 (-1.1% desde el inicio) · mitad/mitad sin LP: -0.53%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 87% | 2 | 19.31 $ | -2.97% (-98%/año) | -1.80% (-92%/año) |
| ±5% | tras 24 h | 68% | 0 | 9.24 $ | +0.17% (+26%/año) | -2.17% (-95%/año) |
| ±10% | al salir | 100% | 0 | 12.51 $ | +0.52% (+107%/año) | -0.95% (-73%/año) |
| ±10% | tras 24 h | 100% | 0 | 12.51 $ | +0.52% (+107%/año) | -0.95% (-73%/año) |
| ±20% | al salir | 100% | 0 | 6.91 $ | -0.02% (-3%/año) | -0.59% (-56%/año) |
| ±20% | tras 24 h | 100% | 0 | 6.91 $ | -0.02% (-3%/año) | -0.59% (-56%/año) |

## BASE ETH 0.05
Precio 1,716.61 (-0.8% desde el inicio) · mitad/mitad sin LP: -0.41%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 87% | 2 | 17.70 $ | -2.89% (-98%/año) | -1.75% (-91%/año) |
| ±5% | tras 24 h | 68% | 0 | 9.43 $ | +0.46% (+90%/año) | -2.23% (-96%/año) |
| ±10% | al salir | 100% | 0 | 12.00 $ | +0.74% (+178%/año) | -1.05% (-77%/año) |
| ±10% | tras 24 h | 100% | 0 | 12.00 $ | +0.74% (+178%/año) | -1.05% (-77%/año) |
| ±20% | al salir | 100% | 0 | 6.43 $ | +0.19% (+30%/año) | -0.60% (-57%/año) |
| ±20% | tras 24 h | 100% | 0 | 6.43 $ | +0.19% (+30%/año) | -0.60% (-57%/año) |

## ARB ETH 0.05
Precio 1,716.62 (-0.8% desde el inicio) · mitad/mitad sin LP: -0.41%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 87% | 2 | 17.13 $ | -2.97% (-98%/año) | -1.83% (-92%/año) |
| ±5% | tras 24 h | 68% | 0 | 9.48 $ | +0.46% (+89%/año) | -2.23% (-96%/año) |
| ±10% | al salir | 100% | 0 | 11.65 $ | +0.70% (+162%/año) | -1.10% (-78%/año) |
| ±10% | tras 24 h | 100% | 0 | 11.65 $ | +0.70% (+162%/año) | -1.10% (-78%/año) |
| ±20% | al salir | 100% | 0 | 6.24 $ | +0.16% (+25%/año) | -0.63% (-58%/año) |
| ±20% | tras 24 h | 100% | 0 | 6.24 $ | +0.16% (+25%/año) | -0.63% (-58%/año) |

## ARB BTC 0.05
Precio 61,128.23 (-0.5% desde el inicio) · mitad/mitad sin LP: -0.23%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 93% | 1 | 11.22 $ | -1.42% (-86%/año) | -1.12% (-79%/año) |
| ±5% | tras 24 h | 78% | 0 | 8.08 $ | +0.52% (+105%/año) | -1.15% (-80%/año) |
| ±10% | al salir | 100% | 0 | 6.85 $ | +0.40% (+74%/año) | -0.51% (-51%/año) |
| ±10% | tras 24 h | 100% | 0 | 6.85 $ | +0.40% (+74%/año) | -0.51% (-51%/año) |
| ±20% | al salir | 100% | 0 | 3.66 $ | +0.08% (+12%/año) | -0.18% (-22%/año) |
| ±20% | tras 24 h | 100% | 0 | 3.66 $ | +0.08% (+12%/año) | -0.18% (-22%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
