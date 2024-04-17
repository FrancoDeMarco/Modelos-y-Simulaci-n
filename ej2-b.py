import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print("Distribución normal:")

# Generar 100 números aleatorios con distribución normal (gaussiana) con media 0 y desvío 1
random_values = np.random.normal(0, 1, 100)

# Calcular la media
media = np.mean(random_values)
print(f'La media de los números generados es: {media:.2f}')

# Calcular la varianza
varianza = np.var(random_values)
print(f'La varianza de los números generados es: {varianza:.2f}')

# Calcular el desvío estándar
desvio_estandar = np.std(random_values)
print(f'El desvío estándar de los números generados es: {desvio_estandar:.2f}')

# Graficar los valores generados
sns.histplot(random_values, kde=True)
plt.title('Distribución normal de números generados')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()
