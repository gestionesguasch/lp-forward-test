# Prueba en vivo de LP concentrado

**Actualizado:** 22/11/2026 17:23 UTC · **2.2 días de datos** · 10 lecturas · huecos: 32

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,714.03 (-1.0% desde el inicio) · mitad/mitad sin LP: -0.50%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 85% | 2 | 18.36 $ | -3.04% (-99%/año) | -1.90% (-96%/año) |
| ±5% | tras 24 h | 62% | 0 | 8.27 $ | +0.11% (+20%/año) | -2.27% (-98%/año) |
| ±10% | al salir | 100% | 0 | 12.00 $ | +0.51% (+132%/año) | -1.00% (-81%/año) |
| ±10% | tras 24 h | 100% | 0 | 12.00 $ | +0.51% (+132%/año) | -1.00% (-81%/año) |
| ±20% | al salir | 100% | 0 | 6.63 $ | -0.01% (-2%/año) | -0.62% (-64%/año) |
| ±20% | tras 24 h | 100% | 0 | 6.63 $ | -0.01% (-2%/año) | -0.62% (-64%/año) |

## BASE ETH 0.05
Precio 1,712.01 (-1.1% desde el inicio) · mitad/mitad sin LP: -0.54%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 85% | 2 | 16.62 $ | -3.08% (-99%/año) | -1.85% (-95%/año) |
| ±5% | tras 24 h | 62% | 0 | 8.33 $ | +0.19% (+37%/año) | -2.33% (-98%/año) |
| ±10% | al salir | 100% | 0 | 11.42 $ | +0.53% (+140%/año) | -1.10% (-84%/año) |
| ±10% | tras 24 h | 100% | 0 | 11.42 $ | +0.53% (+140%/año) | -1.10% (-84%/año) |
| ±20% | al salir | 100% | 0 | 6.12 $ | +0.02% (+3%/año) | -0.63% (-64%/año) |
| ±20% | tras 24 h | 100% | 0 | 6.12 $ | +0.02% (+3%/año) | -0.63% (-64%/año) |

## ARB ETH 0.05
Precio 1,711.97 (-1.1% desde el inicio) · mitad/mitad sin LP: -0.54%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 85% | 2 | 16.03 $ | -3.16% (-99%/año) | -1.93% (-96%/año) |
| ±5% | tras 24 h | 62% | 0 | 8.35 $ | +0.19% (+36%/año) | -2.34% (-98%/año) |
| ±10% | al salir | 100% | 0 | 11.06 $ | +0.49% (+123%/año) | -1.15% (-85%/año) |
| ±10% | tras 24 h | 100% | 0 | 11.06 $ | +0.49% (+123%/año) | -1.15% (-85%/año) |
| ±20% | al salir | 100% | 0 | 5.93 $ | -0.01% (-2%/año) | -0.65% (-66%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.93 $ | -0.01% (-2%/año) | -0.65% (-66%/año) |

## ARB BTC 0.05
Precio 60,909.50 (-0.8% desde el inicio) · mitad/mitad sin LP: -0.41%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 92% | 1 | 10.50 $ | -1.51% (-92%/año) | -1.19% (-86%/año) |
| ±5% | tras 24 h | 73% | 0 | 7.35 $ | +0.24% (+49%/año) | -1.22% (-87%/año) |
| ±10% | al salir | 100% | 0 | 6.47 $ | +0.17% (+33%/año) | -0.55% (-60%/año) |
| ±10% | tras 24 h | 100% | 0 | 6.47 $ | +0.17% (+33%/año) | -0.55% (-60%/año) |
| ±20% | al salir | 100% | 0 | 3.46 $ | -0.12% (-18%/año) | -0.21% (-29%/año) |
| ±20% | tras 24 h | 100% | 0 | 3.46 $ | -0.12% (-18%/año) | -0.21% (-29%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
