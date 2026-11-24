# Prueba en vivo de LP concentrado

**Actualizado:** 24/11/2026 20:50 UTC · **4.4 días de datos** · 16 lecturas · huecos: 56

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,671.32 (-3.5% desde el inicio) · mitad/mitad sin LP: -1.73%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 92% | 2 | 31.39 $ | -2.93% (-92%/año) | -0.75% (-47%/año) |
| ±5% | tras 24 h | 81% | 0 | 21.64 $ | -0.35% (-25%/año) | -1.08% (-60%/año) |
| ±10% | al salir | 100% | 0 | 18.97 $ | -0.32% (-23%/año) | -0.41% (-29%/año) |
| ±10% | tras 24 h | 100% | 0 | 18.97 $ | -0.32% (-23%/año) | -0.41% (-29%/año) |
| ±20% | al salir | 100% | 0 | 10.48 $ | -1.02% (-58%/año) | -0.30% (-22%/año) |
| ±20% | tras 24 h | 100% | 0 | 10.48 $ | -1.02% (-58%/año) | -0.30% (-22%/año) |

## BASE ETH 0.05
Precio 1,675.17 (-3.2% desde el inicio) · mitad/mitad sin LP: -1.60%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 92% | 2 | 29.07 $ | -2.72% (-90%/año) | -0.78% (-48%/año) |
| ±5% | tras 24 h | 81% | 0 | 21.00 $ | -0.09% (-7%/año) | -1.25% (-65%/año) |
| ±10% | al salir | 100% | 0 | 18.03 $ | -0.11% (-9%/año) | -0.55% (-37%/año) |
| ±10% | tras 24 h | 100% | 0 | 18.03 $ | -0.11% (-9%/año) | -0.55% (-37%/año) |
| ±20% | al salir | 100% | 0 | 9.66 $ | -0.82% (-50%/año) | -0.33% (-24%/año) |
| ±20% | tras 24 h | 100% | 0 | 9.66 $ | -0.82% (-50%/año) | -0.33% (-24%/año) |

## ARB ETH 0.05
Precio 1,675.23 (-3.2% desde el inicio) · mitad/mitad sin LP: -1.60%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 92% | 2 | 29.37 $ | -2.71% (-90%/año) | -0.77% (-48%/año) |
| ±5% | tras 24 h | 81% | 0 | 21.94 $ | +0.00% (+0%/año) | -1.17% (-63%/año) |
| ±10% | al salir | 100% | 0 | 18.15 $ | -0.11% (-9%/año) | -0.55% (-37%/año) |
| ±10% | tras 24 h | 100% | 0 | 18.15 $ | -0.11% (-9%/año) | -0.55% (-37%/año) |
| ±20% | al salir | 100% | 0 | 9.73 $ | -0.82% (-50%/año) | -0.33% (-24%/año) |
| ±20% | tras 24 h | 100% | 0 | 9.73 $ | -0.82% (-50%/año) | -0.33% (-24%/año) |

## ARB BTC 0.05
Precio 59,776.91 (-2.7% desde el inicio) · mitad/mitad sin LP: -1.33%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 96% | 1 | 18.78 $ | -1.01% (-57%/año) | -0.64% (-41%/año) |
| ±5% | tras 24 h | 86% | 0 | 15.64 $ | -0.18% (-14%/año) | -0.70% (-44%/año) |
| ±10% | al salir | 100% | 0 | 10.81 $ | -0.49% (-34%/año) | -0.28% (-21%/año) |
| ±10% | tras 24 h | 100% | 0 | 10.81 $ | -0.49% (-34%/año) | -0.28% (-21%/año) |
| ±20% | al salir | 100% | 0 | 5.78 $ | -0.90% (-53%/año) | -0.01% (-1%/año) |
| ±20% | tras 24 h | 100% | 0 | 5.78 $ | -0.90% (-53%/año) | -0.01% (-1%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
