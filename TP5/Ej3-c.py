import numpy as np
import matplotlib.pyplot as plt

# Definir las duraciones de las tareas (distribuciones uniformes)
durations = {
    'A': (2, 4),
    'B': (3, 5),
    'C': (1, 2),
    'D': (4, 8),
    'E': (3, 6),
    'F': (2, 5),
    'G': (2, 4),
    'H': (1, 3),
    'I': (2, 4),
    'J': (2, 3)
}

# Simulación de una corrida del proyecto
def simulate_project():
    A = np.random.uniform(*durations['A'])
    B = np.random.uniform(*durations['B'])
    C = np.random.uniform(*durations['C'])
    D = np.random.uniform(*durations['D'])
    E = np.random.uniform(*durations['E'])
    F = np.random.uniform(*durations['F'])
    G = np.random.uniform(*durations['G'])
    H = np.random.uniform(*durations['H'])
    I = np.random.uniform(*durations['I'])
    J = np.random.uniform(*durations['J'])
    
    # Calcular los tiempos para cada acceso
    t_sup = A + B + D + H + I + J
    t_med = C + F + G + J
    t_inf = E + J
    
    # Tiempo final del proyecto es el máximo de los tres accesos
    return max(t_sup, t_med, t_inf)

# Simulación de experimentos
n_experiments = 30
n_runs = 100
results = np.zeros((n_experiments, n_runs))

for i in range(n_experiments):
    for j in range(n_runs):
        results[i, j] = simulate_project()

# Cálculo del tiempo promedio de finalización del proyecto
mean_times = results.mean(axis=1)
overall_mean = mean_times.mean()
overall_std = mean_times.std()
confidence_interval = 2.57 * overall_std / np.sqrt(n_experiments)

# Evaluar el porcentaje de criticidad de cada tarea (frecuencia de estar en la ruta crítica)
critical_counts = np.zeros(len(durations))

def check_critical(task_durations):
    A, B, C, D, E, F, G, H, I, J = task_durations
    t_sup = A + B + D + H + I + J
    t_med = C + F + G + J
    t_inf = E + J
    max_time = max(t_sup, t_med, t_inf)
    critical_tasks = []

    if t_sup == max_time:
        critical_tasks.extend(['A', 'B', 'D', 'H', 'I', 'J'])
    if t_med == max_time:
        critical_tasks.extend(['C', 'F', 'G', 'J'])
    if t_inf == max_time:
        critical_tasks.extend(['E', 'J'])
        
    return critical_tasks

for i in range(n_experiments):
    for j in range(n_runs):
        task_durations = [np.random.uniform(*durations[task]) for task in 'ABCDEFGHIJ']
        critical_tasks = check_critical(task_durations)
        for task in critical_tasks:
            critical_counts[list(durations.keys()).index(task)] += 1

critical_percentages = critical_counts / (n_experiments * n_runs) * 100

# Graficar el histograma de los tiempos de realización del proyecto (3000 corridas)
plt.figure(figsize=(12, 6))
plt.hist(results.flatten(), bins=30, alpha=0.75, color='blue')
plt.title('Distribución del tiempo de realización del proyecto (3000 corridas)')
plt.xlabel('Tiempo de realización (días)')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Graficar el histograma de los promedios de los 30 experimentos
plt.figure(figsize=(12, 6))
plt.hist(mean_times, bins=10, alpha=0.75, color='green')
plt.title('Distribución de los tiempos promedio de finalización del proyecto (30 experimentos)')
plt.xlabel('Tiempo promedio de realización (días)')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Resultados
print(f"Tiempo promedio de finalización del proyecto: {overall_mean:.2f} días")
print(f"Intervalo de confianza del 99%: ({overall_mean - confidence_interval:.2f}, {overall_mean + confidence_interval:.2f}) días")
print("Porcentaje de criticidad de cada tarea:")
for task, percentage in zip(durations.keys(), critical_percentages):
    print(f"{task}: {percentage:.2f}%")