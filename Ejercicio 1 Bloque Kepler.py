### Ejercicio 1: Tienes datos de ventas mensuales. Escribe un programa que:

# Guarde las ventas de cada mes en variables

enero = 4500
febrero = 5200
marzo = 4800
abril = 6500
mayo = 3600
junio = 4700
julio = 5100
agosto = 4900
septiembre = 2300
octubre = 3600
noviembre = 4100
diciembre = 5800

# Calcule el total y el promedio

total = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + noviembre + diciembre
print(f"El total de ventas es: {total}")

promedio = total / 12
print(f"El promedio de ventas mensual es: {promedio}")

# Identifique el mes con mayores ventas

mes_mas_ventas = max(enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre)
print(f"El maximo de ventas fue: {mes_mas_ventas}")

# Determine si se alcanzó la meta anual (50000)

if total > 50000:
    print("Se alcanzó la meta anual")
else:
    print("No se alcanzó la meta anual")