# Ejercicio 5: Mini proyecto integrador
# Objetivo: Crear un análisis completo desde cero

# Enunciado
# Crea un programa que simule el análisis de una biblioteca durante un mes.

# Datos a generar aleatoriamente (o puedes usar datos fijos):

""" 100 préstamos
Categorías: Ficción, Ensayo, Cómic, Poesía
Días de préstamo: entre 5 y 45 días
Análisis a realizar:

Por categoría:
    Cuántos préstamos
    Promedio de días
    Porcentaje del total

Por estado:
    A tiempo (≤ 21 días)
    Retraso leve (22-30 días)
    Retraso grave (> 30 días)

Penalizaciones:
    Total recaudado en penalizaciones
    Promedio por préstamo con retraso

Top 5:
    Préstamos más largos"""

import random

def generar_datos(n=100):
    categorias = ["ficcion", "ensayo", "comic", "poesia"]
    prestamos = []

    for libro in range(n):
        prestamo = {
            "categoria": random.choice(categorias),
            "dias": random.randint(5, 45)
        }
        prestamos.append(prestamo)
    return prestamos
    pass

datos = generar_datos()
# print(datos)


def analizar_por_categoria(prestamos):
    resultado = {}

    for prestamo in prestamos:
        cat = prestamo["categoria"]

        if cat not in resultado:
            resultado[cat] = 0

        resultado[cat] += 1

    return resultado
analisis = analizar_por_categoria(datos)
# print(analisis)

def analizar_por_dias(prestamos):
    resultado = {}
    dias_totales = 0
    for prestamo in prestamos:
        cat = prestamo["categoria"]
        dias = prestamo["dias"]
        if cat not in resultado:
            resultado[cat] = 0
            dias_totales += dias

        resultado[cat] += dias

    return resultado
analisis_dias = analizar_por_dias(datos)
# print(analisis)


def analizar_promedio_y_porcentaje(conteos, sumas):
    resultado = {}
    total_prestamos = sum(conteos.values())

    for categoria in conteos:
        promedio = sumas[categoria] / conteos[categoria]
        porcentaje = conteos[categoria] / total_prestamos * 100

        resultado[categoria] = {
            "promedio": promedio,
            "porcentaje": porcentaje
        }

    return resultado

promedios = analizar_promedio_y_porcentaje(analisis, analisis_dias)
# print(promedios)

def analizar_por_estado(prestamos):
    a_tiempo = []
    retraso_leve = []
    retraso_grave = []
    for prestamo in prestamos:
        if prestamo["dias"] <= 21:
            a_tiempo.append(prestamo)
        elif prestamo["dias"] < 30:
            retraso_leve.append(prestamo)
        else:
            retraso_grave.append(prestamo)
    return a_tiempo, retraso_leve, retraso_grave
    pass

clasificacion = analizar_por_estado(datos)
a, leve, grave = clasificacion

# print(f"Los libros devueltos a tiempo son {a}")
# print(f"Los libros entregados con un retraso leve son {leve}")
# print(f"Los libros entregados con un retraso grave son {grave}")


def calcular_penalizaciones(prestamos):
    a_tiempo = 0
    retraso_leve = 0
    retraso_grave = 0
    for prestamo in prestamos:
        if prestamo["dias"] <= 21:
            a_tiempo += 0
        elif prestamo["dias"] < 30:
            retraso_leve += 0.5
        else:
            retraso_grave += 1
    return a_tiempo, retraso_leve, retraso_grave     
    pass

total_penalizaciones = calcular_penalizaciones(datos)
a_tiempo, leve_tiempo, grave_tiempo = total_penalizaciones
# print(a_tiempo+leve_tiempo+grave_tiempo)


datos = generar_datos(100)

print("=== ANÁLISIS DE BIBLIOTECA ===\n")

print(f"Hemos analizado {len(datos)} datos de una biblioteca.")

print("\nEn el análisis por categoria, hemos detectado las siguientes conclusiones:")
for categoria, dias in analisis.items():
    print(f" - {categoria.capitalize()}: Numero de prestamos: {dias}")

print("\nY hemos analizado el numero de dias que se prestan por categoria:")
for categoria, dias in analisis_dias.items():
    print(f" - {categoria.capitalize()}: {dias} días acumulados")

print("\nCalculando los promedios y porcentajes por categoría, llegamos a la conclusión de que:")
for categoria, datos_cat in promedios.items():
    print(f" - {categoria.capitalize()}: "
          f"Promedio de días = {datos_cat['promedio']:.2f}, "
          f"Porcentaje = {datos_cat['porcentaje']:.2f}%")

print("\nTambien hemos categorizado los prestamos según su retraso en la devolucion:")
print(f"Los libros devueltos a tiempo son {len(a)}")
print(f"Los libros entregados con un retraso leve son {len(leve)}")
print(f"Los libros entregados con un retraso grave son {len(grave)}")

print(f"\nAdemás, hemos calculado que el total de penalizaciones asciende a {a_tiempo+leve_tiempo+grave_tiempo}")


