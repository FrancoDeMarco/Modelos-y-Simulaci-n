import time
import math
import seaborn as sns
import matplotlib.pyplot as plt

# Función para generar números aleatorios con una distribución probabilística uniforme
def random_with_distribution(min_value, max_value, exponent):
    seed = int(time.time() * 1000000) % 1000000
    random_number = ((seed * 9301 + 49297) % 233280) / 233280.0
    scaled_number = min_value + random_number * (max_value - min_value)
    distributed_number = scaled_number ** exponent
    return round(distributed_number)

# Lista para almacenar los valores generados aleatoriamente
random_values = []

# Generar y almacenar 10 números aleatorios entre 1 y 100 siguiendo una distribución exponencial
for i in range(100):
    random_value = random_with_distribution(1, 100, 1)
    random_values.append(random_value)
    print('Número', i+1, ':', random_value)


#MEDIA
# Calcular la media de los valores generados
media = sum(random_values) / len(random_values)
print(f'La media de los números generados es: {media:.2f}')


#VARIANZA
# Calcular la varianza
varianza = sum((x - media) ** 2 for x in random_values) / len(random_values)
print(f'La varianza de los números generados es: {varianza:.2f}')


#DESVÍO ESTÁNDAR
# Calcular el desvío estándar
desvio_estandar = math.sqrt(varianza)
print(f'El desvío estándar de los números generados es: {desvio_estandar:.2f}')


# GRÁFICO
# Graficar los valores generados
sns.histplot(random_values, kde=True)
plt.title('Distribución uniforme de números generados')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()