import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generar 100 números aleatorios con distribución uniforme en el rango [0, 1]
print("Distribución uniforme")
random_values_uniform = np.random.uniform(0, 1, 100)

# Función de transformación inversa para distribución exponencial
def transform_to_exponential_uniform(uniform_values, beta):
    return -beta * np.log(1 - uniform_values)

# Parámetro beta para la distribución exponencial
beta = 3

# Transformar los valores uniformemente distribuidos en valores exponenciales
exponential_values = transform_to_exponential_uniform(random_values_uniform, beta)

# Calcular la media muestral
media_muestral = np.mean(exponential_values)
print(f'La media muestral es: {media_muestral:.2f}')

# Calcular la varianza muestral
varianza_muestral = np.var(exponential_values, ddof=1)  # Usamos ddof=1 para calcular la varianza muestral
print(f'La varianza muestral es: {varianza_muestral:.2f}')

# Calcular el desvío estándar muestral
desvio_estandar_muestral = np.std(exponential_values, ddof=1)  # Usamos ddof=1 para calcular el desvío estándar muestral
print(f'El desvío estándar muestral es: {desvio_estandar_muestral:.2f}')

# Graficar los valores transformados
sns.histplot(exponential_values, kde=True)
plt.title('Distribución exponencial con parámetro beta=3 (muestra de 100 valores)')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()
