import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
num_experimentos = 60
num_corridas = 100
tiempo_entre_camiones = 15  # minutos
num_camiones = 4

# Función para convertir minutos a formato de minutos y segundos
def minutos_a_minutos_segundos(minutos):
    minutos_enteros = int(minutos)
    segundos = int((minutos - minutos_enteros) * 60)
    return f"{minutos_enteros}:{segundos:02d} minutos"

# Función para simular el tiempo de atención de cada empleado
def tiempo_atencion_empleado(empleado):
    if empleado == 1:
        return np.random.normal(18, 4)
    elif empleado == 2:
        return np.random.exponential(15)
    elif empleado == 3:
        return np.random.exponential(16)
    elif empleado == 4:
        return np.random.normal(14, 3)

# Función para simular una corrida
def simular_corrida():
    tiempos_espera = []
    tiempo_llegada_camion = 0
    for _ in range(num_camiones):
        tiempo_llegada_camion += np.random.exponential(tiempo_entre_camiones)
        tiempos_atencion = [tiempo_atencion_empleado(np.random.randint(1, 5)) for _ in range(4)]
        tiempo_espera = max(0, max(tiempos_atencion) - (tiempo_llegada_camion - tiempo_entre_camiones))
        tiempos_espera.append(tiempo_espera)
    return np.mean(tiempos_espera)

# Simulación de los experimentos
resultados_experimentos = []
for _ in range(num_experimentos):
    tiempos_promedio_corrida = [simular_corrida() for _ in range(num_corridas)]
    resultados_experimentos.append(np.mean(tiempos_promedio_corrida))

# Cálculo del tiempo promedio de espera de los camiones
tiempo_promedio_espera_minutos = np.mean(resultados_experimentos)
tiempo_promedio_espera_formateado = minutos_a_minutos_segundos(tiempo_promedio_espera_minutos)

# Intervalo de confianza del 95%
intervalo_confianza_minutos = np.percentile(resultados_experimentos, [2.5, 97.5])
intervalo_confianza_formateado = [minutos_a_minutos_segundos(tiempo) for tiempo in intervalo_confianza_minutos]

# Histograma de los resultados de los experimentos
plt.hist(resultados_experimentos, bins=15, edgecolor='black')
plt.title('Histograma de tiempos promedio de espera')
plt.xlabel('Tiempo promedio de espera (minutos)')
plt.ylabel('Frecuencia')
plt.show()

# Cálculo del porcentaje de tiempo de ocupación de cada surtidor
tiempo_total_simulacion = num_experimentos * num_corridas * tiempo_entre_camiones
tiempo_ocupacion_empleado = [0] * 4
for _ in range(num_experimentos):
    for _ in range(num_corridas):
        for empleado in range(1, 5):
            tiempo_ocupacion_empleado[empleado-1] += min(tiempo_atencion_empleado(empleado), tiempo_entre_camiones)
porcentaje_ocupacion = [tiempo / tiempo_total_simulacion * 100 for tiempo in tiempo_ocupacion_empleado]

# Imprimir reporte estadístico
print("Reporte Estadístico:")
print("Tiempo promedio de espera de los camiones:", tiempo_promedio_espera_formateado)
print("Intervalo de confianza del 95%:", intervalo_confianza_formateado)
print("Porcentaje de tiempo de ocupación de cada surtidor:")
for empleado, porcentaje in enumerate(porcentaje_ocupacion, start=1):
    print(f"Empleado {empleado}: {porcentaje:.2f}%")