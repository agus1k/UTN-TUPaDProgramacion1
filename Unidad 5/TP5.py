import random

# Ejercicio 1
# Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja

notas = [7.5, 8.0, 6.5, 9.0, 5.5, 7.0, 8.5, 6.0, 9.5, 4.5]

for i in range(len(notas)):
    print(f"Nota del estudiante {i+1}: {notas[i]}")

promedio = sum(notas) / len(notas)
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)

print(f"\nPromedio de notas: {promedio}")
print(f"Nota más alta: {nota_mas_alta}")

# Ejercicio 2
# Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range(5):
    producto = input(("Ingrese un producto: "))
    productos.append(producto)

print(f"Lista ordenada alfabéticamente {sorted(productos)}")

eliminar = input("Qué producto desea eliminar?: ")
productos.remove(eliminar)

print(f"Lista actualizada: {productos}")

# Ejercicio 3
# Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

numeros = []

for i in range(15):
    numeros.append(random.randint(1,100))

pares = []
impares = []

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])

print(f"Cantidad de pares: {len(pares)}. Cantidad de impares: {len(impares)}")

# Ejercicio 4
# Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []

for num in datos:
    if num not in sin_repetidos:
        sin_repetidos.append(num)

print(sin_repetidos)

# Ejercicio 5
# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["Juan", "Mario", "Pedro", "Valentina", "Agustin", "Ian", "Joaquin", "Carlos"]

print("\n".join(estudiantes))
opcion = input("Querés eliminar un estudiante, o agregar uno existente? (A. Agregar | E. Eliminar): ")

if opcion.upper() == "A":
    nombre = input("Ingrese el nombre del estudiante que quiera agregar: ")
    estudiantes.append(nombre.title())
elif opcion.upper() == "E":
    nombre = input("Ingrese el nombre del estudiante que quiera eliminar: ")
    estudiantes.remove(nombre.title())

print("Nueva lista: ")
print("\n".join(estudiantes))

# Ejercicio 6
# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).
 
lista = [6, 4, 2, 5, 7, 8, 9]

ultimo = lista[-1]
rotada = [ultimo] + lista[:-1]

print(f"Lista rotada: {rotada}")

# Ejercicio 7
# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [[18, 36], [14, 30], [20, 40], [21, 37], [17, 23], [22, 38], [25, 35]]

suma_minimas = 0
suma_maximas = 0
amplitud = 0
mayor_amplitud = 0
dia = 0

for i, temp in enumerate(temperaturas, start=1):
    suma_minimas += temp[0]
    suma_maximas += temp[1]
    amplitud = temp[1] - temp[0]

    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia = i

prom_minimas = suma_minimas / len(temperaturas)
prom_maximas = suma_maximas / len(temperaturas)

print(f"Promedio de las temperaturas mínimas: {prom_minimas}")
print(f"Promedio de las temperaturas máximas: {prom_maximas}")
print(f"El día de mayor amplitud fue el día {dia}")

# Ejercicio 8
# Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas = [[6, 7, 9], [4, 3, 6], [10, 9, 10], [6, 6, 7], [7, 7, 8]]

prom_estudiante = 0
suma_mat1 = 0
suma_mat2 = 0
suma_mat3 = 0

for i, nota in enumerate(notas, start=1):
    prom_estudiante = (nota[0] + nota[1] + nota[2]) / 3
    print(f"Promedio del estudiante {i}: {prom_estudiante}")

    suma_mat1 += nota[0]
    suma_mat2 += nota[1]
    suma_mat3 += nota[2]

prom_mat1 = suma_mat1 / 5
prom_mat2 = suma_mat2 / 5
prom_mat3 = suma_mat3 / 5

print(f"Promedio materia 1: {prom_mat1}") 
print(f"Promedio materia 2: {prom_mat2}") 
print(f"Promedio materia 3: {prom_mat3}") 

# Ejercicio 9
# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tablero = [["-","-","-"],["-","-","-"],["-","-","-"]]

for fila in tablero:
    print(fila)

fila = int(input("Jugador 1 (X), ingrese fila (1,3): "))
col = int(input("Jugador 1 (X), ingrese columna (1,3): "))

tablero[fila-1][col-1] = "X"

for fila in tablero:
    print(fila)

fila = int(input("Jugador 2 (O), ingrese fila (1,3): "))
col = int(input("Jugador 2 (O), ingrese columna (1,3): "))

tablero[fila-1][col-1] = "O"

for fila in tablero:
    print(fila)

# # Ejercicio 10
# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [32, 25, 11, 87, 22, 78, 98],   
    [54, 34, 23, 567, 45, 65, 90],  
    [23, 67, 54, 234, 11, 223, 23], 
    [67, 33, 99, 11, 665, 12, 16]   
]

total_prod1 = sum(ventas[0])
total_prod2 = sum(ventas[1])
total_prod3 = sum(ventas[2])
total_prod4 = sum(ventas[3])

mayores_ventas = 0
dia_mayores_ventas = 0

for d in range(7):  
    ventas_dia = ventas[0][d] + ventas[1][d] + ventas[2][d] + ventas[3][d]
    if ventas_dia > mayores_ventas:
        mayores_ventas = ventas_dia
        dia_mayores_ventas = d + 1  

producto_mas_vendido = max(total_prod1, total_prod2, total_prod3, total_prod4)

if producto_mas_vendido == total_prod1:
    producto = 1
elif producto_mas_vendido == total_prod2:
    producto = 2
elif producto_mas_vendido == total_prod3:
    producto = 3
else:
    producto = 4

print(f"Total vendido del producto 1: {total_prod1}")
print(f"Total vendido del producto 2: {total_prod2}")
print(f"Total vendido del producto 3: {total_prod3}")
print(f"Total vendido del producto 4: {total_prod4}")
print(f"Día con mayores ventas: {dia_mayores_ventas}")
print(f"El producto más vendido fue el producto {producto}")
