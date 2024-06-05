import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Parámetros
num_days = 365
hours_per_day = 8
minutes_per_hour = 60
total_minutes_per_day = hours_per_day * minutes_per_hour

# Tiempos de servicio
mean_service_time_cashier1 = 15
std_dev_service_time_cashier1 = 3
mean_service_time_cashier2 = 12

# Tiempo de llegada de clientes
mean_arrival_time = 10

# Simulación
wait_times = []
cashier1_busy_time = []
cashier2_busy_time = []

for day in range(num_days):
    current_time = 0
    queue = []
    cashier1_end_time = 0
    cashier2_end_time = 0
    day_wait_times = []
    cashier1_busy = 0
    cashier2_busy = 0

    while current_time < total_minutes_per_day:
        # Generar el tiempo de llegada del próximo cliente
        arrival_time = np.random.exponential(mean_arrival_time)
        current_time += arrival_time
        if current_time >= total_minutes_per_day:
            break
        queue.append(current_time)

        # Atención por cada cajero
        if queue:
            if current_time >= cashier1_end_time:
                service_time = np.random.normal(mean_service_time_cashier1, std_dev_service_time_cashier1)
                if service_time < 0:
                    service_time = 0
                cashier1_busy += service_time
                cashier1_end_time = current_time + service_time
                arrival = queue.pop(0)
                day_wait_times.append(cashier1_end_time - arrival)

            if queue and current_time >= cashier2_end_time:
                service_time = np.random.exponential(mean_service_time_cashier2)
                cashier2_busy += service_time
                cashier2_end_time = current_time + service_time
                arrival = queue.pop(0)
                day_wait_times.append(cashier2_end_time - arrival)
    
    wait_times.append(np.mean(day_wait_times))
    cashier1_busy_time.append(cashier1_busy / total_minutes_per_day)
    cashier2_busy_time.append(cashier2_busy / total_minutes_per_day)

# Cálculo del intervalo de confianza para el tiempo de espera promedio
confidence_level = 0.95
mean_wait_time = np.mean(wait_times)
sem_wait_time = stats.sem(wait_times)
ci_wait_time = stats.t.interval(confidence_level, num_days-1, loc=mean_wait_time, scale=sem_wait_time)

# Resultados
print(f"Tiempo promedio de espera: {mean_wait_time:.2f} minutos")
print(f"Intervalo de confianza al 95% para el tiempo de espera promedio: ({ci_wait_time[0]:.2f}, {ci_wait_time[1]:.2f}) minutos")

# Porcentaje de tiempo de ocupación de cada caja
mean_cashier1_busy = np.mean(cashier1_busy_time)
mean_cashier2_busy = np.mean(cashier2_busy_time)
print(f"Porcentaje de tiempo de ocupación de la caja 1: {mean_cashier1_busy*100:.2f}%")
print(f"Porcentaje de tiempo de ocupación de la caja 2: {mean_cashier2_busy*100:.2f}%")

# Histograma de los tiempos de espera promedio por día
plt.hist(wait_times, bins=30, edgecolor='k', alpha=0.7)
plt.xlabel('Tiempo promedio de espera (minutos)')
plt.ylabel('Frecuencia')
plt.title('Histograma de tiempos promedio de espera por día')
plt.show()