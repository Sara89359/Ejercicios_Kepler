# Ejercicio 3: Análisis de categorías

# Objetivo: Practicar listas, diccionarios y bucles

# Enunciado
# Tienes una lista de libros prestados con su categoría y días de préstamo:

"""prestamos = [
    {"titulo": "1984", "categoria": "Ficción", "dias": 15},
    {"titulo": "Sapiens", "categoria": "Ensayo", "dias": 22},
    {"titulo": "Watchmen", "categoria": "Cómic", "dias": 18},
    {"titulo": "El Quijote", "categoria": "Ficción", "dias": 30},
    {"titulo": "Breve historia", "categoria": "Ensayo", "dias": 25},
    {"titulo": "Batman", "categoria": "Cómic", "dias": 12}
]"""

# Escribe un programa que:

# Agrupe los préstamos por categoría
# Calcule el promedio de días por categoría
# Identifique la categoría más prestada
# Muestre libros con más de 20 días
   """Pistas
# Crea un diccionario para agrupar por categoría
# Usa un bucle para iterar sobre los préstamos
# Para cada categoría, guarda una lista de días
# Calcula promedios usando sum() y len()"""

prestamos = [
    {"titulo": "1984", "categoria": "Ficción", "dias": 15},
    {"titulo": "Sapiens", "categoria": "Ensayo", "dias": 22},
    {"titulo": "Watchmen", "categoria": "Cómic", "dias": 18},
    {"titulo": "El Quijote", "categoria": "Ficción", "dias": 30},
    {"titulo": "Breve historia", "categoria": "Ensayo", "dias": 25},
    {"titulo": "Batman", "categoria": "Cómic", "dias": 12}
]

# Agrupe los préstamos por categoría

libros = {}

for prestamo in prestamos:
    categoria = prestamo["categoria"]
    titulo = prestamo["titulo"]
    dias = prestamo["dias"]
    if categoria not in libros:
        libros[categoria] = list()
    libros[categoria].append(titulo)
    libros[categoria].append(dias)

print(libros)

# Calcule el promedio de días por categoría

libros2 = {}

for prestamo in prestamos:
    categoria = prestamo["categoria"]
    titulo = prestamo["titulo"]
    dias = prestamo["dias"]
    if categoria not in libros2:
        libros2[categoria] = list()
    libros2[categoria].append(dias)

for categoria, dias in libros2.items():
    numero_de_dias = sum(dias)
    total_de_dias = len(dias)
    promedio = numero_de_dias / total_de_dias
    print(f"El promedio de días de la categoria de {categoria} es de {promedio}")


# Identifique la categoría más prestada

categoria_mas_prestada = ""
max_de_prestamos = 0 

for categoria, dias in libros2.items():
    cantidad = len(dias)
    if cantidad > max_de_prestamos:
        max_de_prestamos = cantidad
        categoria_mas_prestada = categoria
print(f"La categoria más prestada es {categoria} con {max_de_prestamos} prestamos")


# Muestre libros con más de 20 días

for prestamo in prestamos:
    titulo = prestamo["titulo"]
    dias = prestamo["dias"]
    if dias > 20:
        print(f"El libro {titulo} tiene mas de 20 dias, en concreto {dias} dias")