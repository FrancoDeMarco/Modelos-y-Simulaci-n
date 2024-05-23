import numpy as np
import matplotlib.pyplot as plt

# Definición de las distribuciones
def tiempo_tarea(distribucion):
    return np.random.uniform(distribucion[0], distribucion[1])

# Simulación de Monte Carlo
def simulacion_corrida():
    # Acceso Superior
    tiempo_A = tiempo_tarea((1, 5))
    tiempo_B = tiempo_tarea((1, 3))
    tiempo_C = tiempo_tarea((1, 3))
    tiempo_superior = tiempo_A + tiempo_B + tiempo_C

    # Acceso Medio
    tiempo_D = tiempo_tarea((1, 6))
    tiempo_E = tiempo_tarea((6, 12))
    tiempo_F1 = tiempo_tarea((5, 10))
    tiempo_medio = tiempo_A + tiempo_D + tiempo_E + tiempo_F1

    # Acceso Inferior
    tiempo_G = tiempo_tarea((10, 15))
    tiempo_inferior = tiempo_F1 + tiempo_G

    # Determinamos el tiempo total del proyecto
    tiempo_total = max(tiempo_superior, tiempo_medio, tiempo_inferior)
    return tiempo_total, tiempo_superior, tiempo_medio, tiempo_inferior

# Parámetros de la simulación
num_experimentos = 30
num_corridas = 100

# Almacenar resultados
resultados_totales = []
resultados_experimentos = []

for _ in range(num_experimentos):
    tiempos_corridas = []
    for _ in range(num_corridas):
        tiempo_total, tiempo_superior, tiempo_medio, tiempo_inferior = simulacion_corrida()
        tiempos_corridas.append(tiempo_total)
        resultados_totales.append(tiempo_total)
    resultados_experimentos.append(np.mean(tiempos_corridas))

# Cálculo de estadísticas
promedio_finalizacion = np.mean(resultados_totales)
ic_99 = 2.57 * (np.std(resultados_totales) / np.sqrt(len(resultados_totales)))

# Cálculo del porcentaje de criticidad
criticidad_superior = sum(1 for t in resultados_totales if t == tiempo_superior) / len(resultados_totales) * 100
criticidad_medio = sum(1 for t in resultados_totales if t == tiempo_medio) / len(resultados_totales) * 100
criticidad_inferior = sum(1 for t in resultados_totales if t == tiempo_inferior) / len(resultados_totales) * 100

# Graficar histogramas
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.hist(resultados_totales, bins=30, color='blue', alpha=0.7)
plt.title('Distribución del tiempo de realización del proyecto (3000 corridas)')
plt.xlabel('Tiempo total')
plt.ylabel('Frecuencia')

plt.subplot(1, 2, 2)
plt.hist(resultados_experimentos, bins=30, color='green', alpha=0.7)
plt.title('Distribución de los promedios de los 30 experimentos')
plt.xlabel('Tiempo promedio')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Resultados
(promedio_finalizacion, ic_99, criticidad_superior, criticidad_medio, criticidad_inferior)