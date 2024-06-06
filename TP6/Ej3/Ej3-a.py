import numpy as np

# Parámetros del problema
lambda_demanda = 37
costo_unitario = 450
costo_orden = 93
lead_time = 3
costo_almacenamiento = 35
costo_faltante = 20
cantidad_ordenar = 100
dias = 365

# Estrategias de reorden
puntos_reorden = [30, 15, 40]

# Función para simular una estrategia
def simular_estrategia(punto_reorden):
    inventario = 150
    costo_total_almacenamiento = 0
    costo_total_faltantes = 0
    costo_total_pedidos = 0
    pedidos_pendientes = []

    for dia in range(dias):
        # Generar la demanda del día
        demanda = np.random.poisson(lambda_demanda)

        # Verificar y procesar los pedidos pendientes
        for i, (cantidad, dias_restantes) in enumerate(pedidos_pendientes):
            if dias_restantes == 0:
                inventario += cantidad
            else:
                pedidos_pendientes[i] = (cantidad, dias_restantes - 1)
        
        # Actualizar lista de pedidos pendientes eliminando los completados
        pedidos_pendientes = [(cantidad, dias_restantes) for cantidad, dias_restantes in pedidos_pendientes if dias_restantes > 0]

        # Calcular la demanda satisfecha y el inventario restante
        if inventario >= demanda:
            inventario -= demanda
        else:
            costo_total_faltantes += (demanda - inventario) * costo_faltante
            inventario = 0

        # Calcular el costo de almacenamiento
        costo_total_almacenamiento += inventario * costo_almacenamiento

        # Realizar pedido si el inventario está en o por debajo del punto de reorden
        if inventario <= punto_reorden:
            pedidos_pendientes.append((cantidad_ordenar, lead_time))
            costo_total_pedidos += cantidad_ordenar * costo_orden

    costo_total = costo_total_almacenamiento + costo_total_faltantes + costo_total_pedidos
    return costo_total

# Simulación para cada estrategia
resultados = {}
for punto_reorden in puntos_reorden:
    costo_total = simular_estrategia(punto_reorden)
    resultados[punto_reorden] = costo_total

# Mostrar los resultados
for punto_reorden, costo_total in resultados.items():
    print(f"Estrategia de reorden en {punto_reorden} unidades: Costo total anual = ${costo_total:.2f}")
