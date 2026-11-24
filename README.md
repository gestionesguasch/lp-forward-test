# Prueba en vivo de LP concentrado

**Actualizado:** 24/11/2026 10:30 UTC · **3.9 días de datos** · 15 lecturas · huecos: 52

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,684.21 (-2.7% desde el inicio) · mitad/mitad sin LP: -1.36%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 92% | 2 | 28.68 $ | -2.78% (-93%/año) | -0.99% (-60%/año) |
| ±5% | tras 24 h | 78% | 0 | 18.86 $ | -0.02% (-2%/año) | -1.33% (-71%/año) |
| ±10% | al salir | 100% | 0 | 17.52 $ | +0.03% (+3%/año) | -0.55% (-40%/año) |
| ±10% | tras 24 h | 100% | 0 | 17.52 $ | +0.03% (+3%/año) | -0.55% (-40%/año) |
| ±20% | al salir | 100% | 0 | 9.68 $ | -0.66% (-46%/año) | -0.37% (-29%/año) |
| ±20% | tras 24 h | 100% | 0 | 9.68 $ | -0.66% (-46%/año) | -0.37% (-29%/año) |

## BASE ETH 0.05
Precio 1,683.17 (-2.7% desde el inicio) · mitad/mitad sin LP: -1.37%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 92% | 2 | 25.95 $ | -2.80% (-93%/año) | -1.08% (-64%/año) |
| ±5% | tras 24 h | 78% | 0 | 17.82 $ | -0.03% (-3%/año) | -1.56% (-77%/año) |
| ±10% | al salir | 100% | 0 | 16.37 $ | +0.03% (+2%/año) | -0.71% (-48%/año) |
| ±10% | tras 24 h | 100% | 0 | 16.37 $ | +0.03% (+2%/año) | -0.71% (-48%/año) |
| ±20% | al salir | 100% | 0 | 8.78 $ | -0.64% (-45%/año) | -0.42% (-32%/año) |
| ±20% | tras 24 h | 100% | 0 | 8.78 $ | -0.64% (-45%/año) | -0.42% (-32%/año) |

## ARB ETH 0.05
Precio 1,683.15 (-2.7% desde el inicio) · mitad/mitad sin LP: -1.37%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 92% | 2 | 26.06 $ | -2.81% (-93%/año) | -1.09% (-64%/año) |
| ±5% | tras 24 h | 78% | 0 | 18.56 $ | +0.04% (+4%/año) | -1.50% (-75%/año) |
| ±10% | al salir | 100% | 0 | 16.39 $ | +0.02% (+2%/año) | -0.72% (-49%/año) |
| ±10% | tras 24 h | 100% | 0 | 16.39 $ | +0.02% (+2%/año) | -0.72% (-49%/año) |
| ±20% | al salir | 100% | 0 | 8.78 $ | -0.65% (-45%/año) | -0.43% (-33%/año) |
| ±20% | tras 24 h | 100% | 0 | 8.78 $ | -0.65% (-45%/año) | -0.43% (-33%/año) |

## ARB BTC 0.05
Precio 59,957.03 (-2.4% desde el inicio) · mitad/mitad sin LP: -1.19%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 1 | 16.59 $ | -1.15% (-66%/año) | -0.84% (-54%/año) |
| ±5% | tras 24 h | 85% | 0 | 13.45 $ | -0.18% (-15%/año) | -0.90% (-57%/año) |
| ±10% | al salir | 100% | 0 | 9.67 $ | -0.42% (-32%/año) | -0.38% (-30%/año) |
| ±10% | tras 24 h | 100% | 0 | 9.67 $ | -0.42% (-32%/año) | -0.38% (-30%/año) |
| ±20% | al salir | 100% | 0 | 5.17 $ | -0.80% (-52%/año) | -0.06% (-5%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.17 $ | -0.80% (-52%/año) | -0.06% (-5%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
