import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parámetros iniciales
capacidad_produccion = 130
media_demanda = 150
desvio_demanda = 25
costo_mantenimiento = 70
dias_habiles = 250
anos_simulacion = 30
dias_totales = dias_habiles * anos_simulacion
inventario_inicial = 90
niveles_minimos_inventario = [50, 60, 70, 80]
simulaciones = 1000

# Función para simular el proceso
def simular_produccion(nivel_minimo_inventario):
    inventario = inventario_inicial
    turnos_adicionales = 0
    costos_mantenimiento = 0
    
    for _ in range(dias_totales):
        demanda = np.random.normal(media_demanda, desvio_demanda)
        demanda = max(0, demanda)  # Asegurar que la demanda no sea negativa
        inventario -= demanda
        if inventario < nivel_minimo_inventario:
            inventario += capacidad_produccion
            turnos_adicionales += 1
        costos_mantenimiento += max(0, inventario) * costo_mantenimiento
        inventario += capacidad_produccion  # Producción regular
        
    turnos_adicionales_promedio = turnos_adicionales / anos_simulacion
    costo_mantenimiento_promedio = costos_mantenimiento / anos_simulacion
    
    return round(turnos_adicionales_promedio), costo_mantenimiento_promedio

# Simular para diferentes niveles mínimos de inventario
resultados = {}
for nivel_minimo in niveles_minimos_inventario:
    costos_anuales = []
    for _ in range(simulaciones):
        _, costo_promedio = simular_produccion(nivel_minimo)
        costos_anuales.append(costo_promedio)
    
    promedio_costos = np.mean(costos_anuales)
    intervalo_confianza = stats.norm.interval(0.95, loc=promedio_costos, scale=np.std(costos_anuales, ddof=1)/np.sqrt(simulaciones))
    
    resultados[nivel_minimo] = {
        'Promedio de costos anuales': promedio_costos,
        'Intervalo de confianza al 95%': intervalo_confianza,
        'Costos anuales': costos_anuales
    }

# Mostrar resultados y graficar histogramas
for nivel_minimo, resultado in resultados.items():
    print(f"Nivel mínimo de inventario: {nivel_minimo}")
    print(f"Promedio de costos anuales: ${resultado['Promedio de costos anuales']:.2f}")
    print(f"Intervalo de confianza al 95%: (${resultado['Intervalo de confianza al 95%'][0]:.2f}, ${resultado['Intervalo de confianza al 95%'][1]:.2f})")
    print()
    
    # Graficar histogramas
    plt.figure(figsize=(10, 6))
    plt.hist(resultado['Costos anuales'], bins=30, alpha=0.75, color='blue', edgecolor='black')
    plt.title(f"Histograma de Costos Anuales para Nivel Mínimo de Inventario: {nivel_minimo}")
    plt.xlabel("Costo Anual de Mantenimiento")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.show()