# Prueba en vivo de LP concentrado

**Actualizado:** 26/11/2026 04:58 UTC · **5.7 días de datos** · 20 lecturas · huecos: 72

Cada ~5 min GitHub lee de la blockchain las comisiones reales de 4 pools de Uniswap v3 y simula posiciones virtuales de 1000 $ (no se mueve dinero). **SIN cobertura** = solo el LP. **CON cobertura** = LP + corto en Hyperliquid del mismo tamaño (quita la direccion del precio, incluye funding real; haría falta ~30 % extra de margen).

Lo que buscamos: **CON cobertura positivo y estable durante 2-3 semanas.** El anualizado solo aparece a partir de 1 día y con pocos dias exagera: fíjate tambien en el %.

## BASE ETH 0.30
Precio 1,700.16 (-1.8% desde el inicio) · mitad/mitad sin LP: -0.90%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 94% | 2 | 39.56 $ | -1.24% (-55%/año) | -0.66% (-34%/año) |
| ±5% | tras 24 h | 78% | 0 | 26.82 $ | +1.45% (+152%/año) | -1.14% (-52%/año) |
| ±10% | al salir | 100% | 0 | 23.33 $ | +1.18% (+113%/año) | -0.42% (-23%/año) |
| ±10% | tras 24 h | 100% | 0 | 23.33 $ | +1.18% (+113%/año) | -0.42% (-23%/año) |
| ±20% | al salir | 100% | 0 | 12.89 $ | +0.18% (+12%/año) | -0.29% (-17%/año) |
| ±20% | tras 24 h | 100% | 0 | 12.89 $ | +0.18% (+12%/año) | -0.29% (-17%/año) |

## BASE ETH 0.05
Precio 1,698.70 (-1.8% desde el inicio) · mitad/mitad sin LP: -0.92%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 94% | 2 | 36.99 $ | -1.31% (-57%/año) | -0.78% (-40%/año) |
| ±5% | tras 24 h | 78% | 0 | 26.01 $ | +1.46% (+153%/año) | -1.21% (-54%/año) |
| ±10% | al salir | 100% | 0 | 22.23 $ | +1.17% (+111%/año) | -0.58% (-31%/año) |
| ±10% | tras 24 h | 100% | 0 | 22.23 $ | +1.17% (+111%/año) | -0.58% (-31%/año) |
| ±20% | al salir | 100% | 0 | 11.92 $ | +0.18% (+12%/año) | -0.36% (-20%/año) |
| ±20% | tras 24 h | 100% | 0 | 11.92 $ | +0.18% (+12%/año) | -0.36% (-20%/año) |

## ARB ETH 0.05
Precio 1,698.90 (-1.8% desde el inicio) · mitad/mitad sin LP: -0.92%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 94% | 2 | 37.77 $ | -1.25% (-55%/año) | -0.73% (-37%/año) |
| ±5% | tras 24 h | 78% | 0 | 27.23 $ | +1.58% (+173%/año) | -1.10% (-51%/año) |
| ±10% | al salir | 100% | 0 | 22.60 $ | +1.21% (+116%/año) | -0.56% (-30%/año) |
| ±10% | tras 24 h | 100% | 0 | 22.60 $ | +1.21% (+116%/año) | -0.56% (-30%/año) |
| ±20% | al salir | 100% | 0 | 12.12 $ | +0.20% (+14%/año) | -0.34% (-20%/año) |
| ±20% | tras 24 h | 100% | 0 | 12.12 $ | +0.20% (+14%/año) | -0.34% (-20%/año) |

## ARB BTC 0.05
Precio 60,932.03 (-0.8% desde el inicio) · mitad/mitad sin LP: -0.39%

| Rango | Reajuste | En rango | Reajustes | Comisiones | SIN cobertura | CON cobertura |
|---|---|---|---|---|---|---|
| ±5% | al salir | 97% | 1 | 24.73 $ | -0.09% (-6%/año) | -1.00% (-47%/año) |
| ±5% | tras 24 h | 83% | 0 | 19.33 $ | +1.46% (+154%/año) | -1.11% (-51%/año) |
| ±10% | al salir | 100% | 0 | 13.94 $ | +0.94% (+82%/año) | -0.49% (-27%/año) |
| ±10% | tras 24 h | 100% | 0 | 13.94 $ | +0.94% (+82%/año) | -0.49% (-27%/año) |
| ±20% | al salir | 100% | 0 | 7.45 $ | +0.30% (+21%/año) | -0.17% (-11%/año) |
| ±20% | tras 24 h | 100% | 0 | 7.45 $ | +0.30% (+21%/año) | -0.17% (-11%/año) |

---
Datos: `lp_forward_data/` (samples.csv cada lectura, snapshots.csv cada hora, state.json). Código: `lp_forward_test.py`. Se ejecuta solo con GitHub Actions (`.github/workflows/lp.yml`).
