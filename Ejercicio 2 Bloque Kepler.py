# Ejercicio 2: Clasificador de préstamos

# Enunciado
# Crea una función que clasifique préstamos según días transcurridos:

# 0-21 días: "A tiempo"
# 22-30 días: "Retraso leve" (penalización: 0.50€/día extra)
# Más de 30 días: "Retraso grave" (penalización: 1.00€/día extra)

# Luego procesa una lista de préstamos y muestra estadísticas.

"""def clasificar_prestamo(dias):
    # Tu código aquí
    pass

# Datos de prueba
prestamos_dias = [15, 22, 18, 35, 25, 12, 40, 19, 28, 33]"""

"""Pistas
La función debe devolver un diccionario con estado y penalizacion
Usa un bucle for para procesar la lista
Cuenta cuántos están en cada categoría
Calcula la penalización total"""

# Procesar y mostrar estadísticas

# Datos de prueba
prestamos_dias = [15, 22, 18, 35, 25, 12, 40, 19, 28, 33]

def clasificar_prestamo(dias):
    if dias <= 21:
        estado = "a tiempo"
        penalizacion = 0
    elif dias >=22 and dias<30:
        estado = "retraso leve"
        limite = dias - 22
        penalizacion = 0.5 * limite
    else:
        estado = "retraso grave"
        limite = dias - 30
        penalizacion = 1 * limite
    return{
        "Estado": estado, 
        "Penalizacion": penalizacion
        }

a_tiempo = 0
retraso_leve = 0
retraso_grave = 0
penalizacion_total = 0

for dias in prestamos_dias:
    estadisticas = clasificar_prestamo(dias)
    estado = estadisticas["Estado"]
    penalizacion = estadisticas["Penalizacion"]
    if estado == "a tiempo":
        a_tiempo +=1
        penalizacion_total += penalizacion
    elif estado == "retraso leve":
        retraso_leve +=1
        penalizacion_total += penalizacion
    else:
        retraso_grave +=1 
        penalizacion_total += penalizacion

print(estadisticas)

print(f"Hay {a_tiempo} prestamos devueltos a tiempo")
print(f"Hay {retraso_leve} prestamos entregados con un retraso leve")
print(f"Hay {retraso_grave} prestamos entregados con retraso grave")

print(f"La penalizacion total es de {penalizacion_total} euros")