import numpy as np

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
    turnos_promedio, costo_promedio = simular_produccion(nivel_minimo)
    resultados[nivel_minimo] = {
        'Turnos adicionales promedio por año': turnos_promedio,
        'Costo de mantenimiento promedio anual': costo_promedio
    }

# Mostrar resultados
for nivel_minimo, resultado in resultados.items():
    print(f"Nivel mínimo de inventario: {nivel_minimo}")
    print(f"Turnos adicionales promedio por año: {resultado['Turnos adicionales promedio por año']}")
    print(f"Costo de mantenimiento promedio anual: ${resultado['Costo de mantenimiento promedio anual']:.2f}")
    print()