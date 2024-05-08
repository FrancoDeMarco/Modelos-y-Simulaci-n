import numpy as np

def calcular_intervalo_confianza(media_muestral, desviacion_estandar_poblacional, tamano_muestra):
    # Obtener el valor crítico z para un 99% de confianza
    z = 2.576
    
    # Calcular el error estándar
    error_estandar = desviacion_estandar_poblacional / np.sqrt(tamano_muestra)
    
    # Calcular el intervalo de confianza
    margen_error = z * error_estandar
    limite_inferior = media_muestral - margen_error
    limite_superior = media_muestral + margen_error
    
    return limite_inferior, limite_superior

# Ejemplo de uso
media_muestral = 3
desviacion_estandar_poblacional = 0.5
tamano_muestra = 10000

limite_inferior, limite_superior = calcular_intervalo_confianza(media_muestral, desviacion_estandar_poblacional, tamano_muestra)
print("Intervalo de confianza para la media poblacional:", (limite_inferior, limite_superior))
