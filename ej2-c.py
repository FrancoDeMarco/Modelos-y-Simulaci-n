import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


print("Distribución de Poisson:")
# Generar 100 números aleatorios con distribución de Poisson con parámetro λ = 6
random_values = np.random.poisson(lam=6, size=100)

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
plt.title('Distribución de Poisson de números generados')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()