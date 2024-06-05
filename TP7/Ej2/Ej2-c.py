import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Parámetros
num_días = 365
horas_por_día = 8
minutos_por_hora = 60
total_minutos_por_día = horas_por_día * minutos_por_hora

# Tiempos de servicio
media_tiempo_servicio_cajero1 = 15
desviación_estándar_tiempo_servicio_cajero1 = 3
media_tiempo_servicio_cajero2 = 12
media_tiempo_servicio_cajero3 = 14
desviación_estándar_tiempo_servicio_cajero3 = 6
media_tiempo_servicio_cajero4 = 14  # Nuevo cajero
desviación_estándar_tiempo_servicio_cajero4 = 6  # Nuevo cajero

# Tiempo de llegada de clientes
media_tiempo_llegada = 10

# Simulación
tiempos_espera = []
tiempo_ocupado_cajero1 = []
tiempo_ocupado_cajero2 = []
tiempo_ocupado_cajero3 = []
tiempo_ocupado_cajero4 = []  # Nuevo cajero

for día in range(num_días):
    tiempo_actual = 0
    cola = []
    fin_tiempo_cajero1 = 0
    fin_tiempo_cajero2 = 0
    fin_tiempo_cajero3 = 0
    fin_tiempo_cajero4 = 0  # Nuevo cajero
    tiempos_espera_día = []
    ocupación_cajero1 = 0
    ocupación_cajero2 = 0
    ocupación_cajero3 = 0
    ocupación_cajero4 = 0  # Nuevo cajero

    while tiempo_actual < total_minutos_por_día:
        # Generar el tiempo de llegada del próximo cliente
        tiempo_llegada = np.random.exponential(media_tiempo_llegada)
        tiempo_actual += tiempo_llegada
        if tiempo_actual >= total_minutos_por_día:
            break
        cola.append(tiempo_actual)

        # Atención por cada cajero
        if cola:
            if tiempo_actual >= fin_tiempo_cajero1:
                tiempo_servicio = np.random.normal(media_tiempo_servicio_cajero1, desviación_estándar_tiempo_servicio_cajero1)
                if tiempo_servicio < 0:
                    tiempo_servicio = 0
                ocupación_cajero1 += tiempo_servicio
                fin_tiempo_cajero1 = tiempo_actual + tiempo_servicio
                llegada = cola.pop(0)
                tiempos_espera_día.append(fin_tiempo_cajero1 - llegada)

            elif cola and tiempo_actual >= fin_tiempo_cajero2:
                tiempo_servicio = np.random.exponential(media_tiempo_servicio_cajero2)
                ocupación_cajero2 += tiempo_servicio
                fin_tiempo_cajero2 = tiempo_actual + tiempo_servicio
                llegada = cola.pop(0)
                tiempos_espera_día.append(fin_tiempo_cajero2 - llegada)
            
            elif cola and tiempo_actual >= fin_tiempo_cajero3:
                tiempo_servicio = np.random.normal(media_tiempo_servicio_cajero3, desviación_estándar_tiempo_servicio_cajero3)
                if tiempo_servicio < 0:
                    tiempo_servicio = 0
                ocupación_cajero3 += tiempo_servicio
                fin_tiempo_cajero3 = tiempo_actual + tiempo_servicio
                llegada = cola.pop(0)
                tiempos_espera_día.append(fin_tiempo_cajero3 - llegada)
                
            elif cola and tiempo_actual >= fin_tiempo_cajero4:
                tiempo_servicio = np.random.normal(media_tiempo_servicio_cajero4, desviación_estándar_tiempo_servicio_cajero4)
                if tiempo_servicio < 0:
                    tiempo_servicio = 0
                ocupación_cajero4 += tiempo_servicio
                fin_tiempo_cajero4 = tiempo_actual + tiempo_servicio
                llegada = cola.pop(0)
                tiempos_espera_día.append(fin_tiempo_cajero4 - llegada)
    
    tiempos_espera.append(np.mean(tiempos_espera_día))
    tiempo_ocupado_cajero1.append(ocupación_cajero1 / total_minutos_por_día)
    tiempo_ocupado_cajero2.append(ocupación_cajero2 / total_minutos_por_día)
    tiempo_ocupado_cajero3.append(ocupación_cajero3 / total_minutos_por_día)
    tiempo_ocupado_cajero4.append(ocupación_cajero4 / total_minutos_por_día)

# Cálculo del intervalo de confianza para el tiempo de espera promedio
nivel_confianza = 0.95
media_tiempo_espera = np.mean(tiempos_espera)
sem_tiempo_espera = stats.sem(tiempos_espera)
ic_tiempo_espera = stats.t.interval(nivel_confianza, num_días-1, loc=media_tiempo_espera, scale=sem_tiempo_espera)

# Resultados
print(f"Tiempo promedio de espera: {int(media_tiempo_espera)} minutos y {int((media_tiempo_espera - int(media_tiempo_espera)) * 60):02d} segundos")
print(f"Intervalo de confianza al 95% para el tiempo de espera promedio: ({int(ic_tiempo_espera[0])} minutos y {int((ic_tiempo_espera[0] - int(ic_tiempo_espera[0])) * 60):02d} segundos, {int(ic_tiempo_espera[1])} minutos y {int((ic_tiempo_espera[1] - int(ic_tiempo_espera[1])) * 60):02d} segundos)")

# Porcentaje de tiempo de ocupación de cada caja
mean_cashier1_busy = np.mean(tiempo_ocupado_cajero1)
mean_cashier2_busy = np.mean(tiempo_ocupado_cajero2)
mean_cashier3_busy = np.mean(tiempo_ocupado_cajero3)
mean_cashier4_busy = np.mean(tiempo_ocupado_cajero4)
print(f"Porcentaje de tiempo de ocupación de la caja 1: {mean_cashier1_busy*100:.2f}%")
print(f"Porcentaje de tiempo de ocupación de la caja 2: {mean_cashier2_busy*100:.2f}%")
print(f"Porcentaje de tiempo de ocupación de la caja 3: {mean_cashier3_busy*100:.2f}%")
print(f"Porcentaje de tiempo de ocupación de la caja 4: {mean_cashier4_busy*100:.2f}%")

# Histograma de los tiempos de espera promedio por día
plt.hist(tiempos_espera, bins=30, edgecolor='k', alpha=0.7)
plt.xlabel('Tiempo promedio de espera (minutos)')
plt.ylabel('Frecuencia')
plt.title('Histograma de tiempos promedio de espera por día')
plt.show()