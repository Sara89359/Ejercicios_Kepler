# Ejercicio 4: Procesador de datos
# Objetivo: Integrar todo (funciones, estructuras, validación)

# Enunciado
# Crea un sistema que procese datos de ventas con las siguientes funciones:

"""def limpiar_datos(ventas):
    "Elimina valores negativos o None"
    pass

def calcular_estadisticas(ventas):
    "Devuelve dict con total, promedio, max, min"
    pass

def clasificar_ventas(ventas, umbral_bajo, umbral_alto):
    "Devuelve dict con ventas bajas, medias, altas"
    pass

def generar_reporte(ventas):
    "Usa las funciones anteriores y muestra reporte completo"
    pass"""

# Datos de prueba (con valores inválidos):

ventas_brutas = [1500, -200, 2500, None, 3000, 0, 4500, -100, 2800, 5000]

# Requerimientos

"""limpiar_datos: Filtrar valores válidos (> 0 y no None)
calcular_estadisticas: Total, promedio, máximo, mínimo
clasificar_ventas:
Baja: < umbral_bajo
Media: entre umbrales
Alta: >= umbral_alto
generar_reporte: Llamar todas las funciones y mostrar resultados formateados"""

# Salida esperada aproximada: 

"""=== REPORTE DE VENTAS ===

Datos procesados: 7 ventas válidas (3 inválidas eliminadas)

Estadísticas:
  Total: 21800
  Promedio: 3114.29
  Máximo: 5000
  Mínimo: 1500

Clasificación:
  Ventas bajas (< 2000): 1 (14.3%)
  Ventas medias: 4 (57.1%)
  Ventas altas (>= 4000): 2 (28.6%)"""

## A partir de aqui empieza mi trabajo:


# Limpiar_datos: Filtrar valores válidos (> 0 y no None)


def limpiar_datos(ventas):
    ventas_limpias = []
    for venta in ventas:
        if venta != None and venta > 0: 
            ventas_limpias.append(venta)
    return ventas_limpias
ventas_limpias = limpiar_datos(ventas_brutas)
print(ventas_limpias)

# calcular_estadisticas: Total, promedio, máximo, mínimo

def calcular_estadisticas(ventas):
    elementos = len(ventas)
    total = sum(ventas)
    promedio = total / elementos
    maximo = max(ventas)
    minimo = min(ventas)
    return "Tenemos unas ganancias de ", total, "Un promedio de ganancias de ", promedio,\
             "Con un maximo de ", maximo, "y un minimo de ", minimo    
    pass
estadisticas = calcular_estadisticas(ventas_limpias)


# clasificar_ventas:

def clasificar_ventas(ventas):
    ventas_bajas = []
    ventas_altas = []
    ventas_medias = []
    total = sum(ventas)
    for venta in ventas:
            if venta <2000:
                ventas_bajas.append(venta)
            elif venta > 4000:
                ventas_altas.append(venta)
            else:
                ventas_medias.append(venta)
    return {
        "Ventas bajas (<2000): ": len(ventas_bajas),
        "Ventas medias: ": len(ventas_medias),
        "Ventas altas (>4000): ": len(ventas_altas)
    }
clasificacion = clasificar_ventas(ventas_limpias)

for titulo, cantidad in clasificacion.items():
    print(f"{titulo}{cantidad}")



# generar_reporte: Llamar todas las funciones y mostrar resultados formateados

print("=== REPORTE DE VENTAS ===\n")
print(f"Hemos analizado {len(ventas_limpias)} ventas con datos válidos")

print("Estadísticas:")
print(estadisticas)

print("Clasificación:")
print(clasificacion)
