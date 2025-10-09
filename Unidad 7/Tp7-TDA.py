# Ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450 }

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# Ejercicio 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# Ejercicio 3

frutas = list(precios_frutas.keys())

print(frutas)

# Ejercicio 4

contactos = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ").title()
    numero = input("Ingrese el número del contacto: ")

    contactos[nombre] = numero

nombre_busqueda = input("Ingrese el contacto que desee buscar: ").title()

if nombre_busqueda in contactos:
    print(contactos[nombre_busqueda])
else:
    print("El contacto no se encuentra en la lista.")

# Ejercicio 5

frase = input("Ingrese una frase: ").lower()

palabras = frase.split()

palabras_unicas = set(palabras)
print(palabras_unicas)

recuento = {}

for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print(recuento)

# Ejercicio 6

alumnos = {}

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    nota1 = int(input("Ingrese la primera nota: "))
    nota2 = int(input("Ingrese la segunda nota: "))
    nota3 = int(input("Ingrese la tercera nota: "))

    notas = nota1, nota2, nota3

    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio {promedio}")

# Ejercicio 7

parcial1 = {9, 8, 12, 43 ,23}
parcial2 = {21, 9, 8, 66, 23}

print(f"Alumnos que aprobaron ambos parciales: {parcial1 & parcial2}")
print(f"Alumnos que aprobaron solo un parcial: {parcial1 ^ parcial2}")
print(f"Alumnos que aprobaron al menos un parcial: {parcial1 | parcial2}")

# Ejercicio 8

opcion = 0

productos = {
    "Teclado": 300,
    "Mouse": 200,
    "Monitor": 150,
    "Auriculares": 100,
    "Silla ergonómica": 50
}

def verificar_producto(producto, diccionario):
    return producto in diccionario

while True:
    opcion = int(input("""
    Ingresa la opción:
    1. Consultar stock
    2. Agregar unidades al stock
    3. Agregar un nuevo producto  
    4. Salir                 
    """))

    if opcion == 1:
        consulta = input("De qué producto desea consultar el stock?: ")
        if not verificar_producto(consulta, productos):
            print("Producto no encontrado")
        else:
            print(productos[consulta])
    elif opcion == 2:
        consulta = input("A qué producto desea agregarle unidades?: ")
        if not verificar_producto(consulta, productos):
            print("Producto no encontrado")
        else:
            cantidad = int(input("Ingrese la cantidad de stock que desee sumar: "))
            productos[consulta] = productos.get(consulta) + cantidad
    elif opcion == 3:
        consulta = input("Qué producto desea agregar?: ")
        if verificar_producto(consulta, productos):
            print("El producto ya se encuentra en el catálogo")
        else:
            cantidad = int(input("Ingrese la cantidad de stock que desee agregar: "))
            productos[consulta] = cantidad
            print("Producto agregado con éxito!")
    elif opcion == 4:
        break

print(productos)

# Ejercicio 9

agenda = {
    ("lunes", "10:30"): "Gym",
    ("martes", "11:30"): "Reunión",
    ("domingo", "21:00"): "Partido de River",
}

dia = input("Ingrese el dia para el que desea consultar la actividad: ").lower()
hora = input("Ingrese la hora del dia especificado: ")

dia_hora = dia, hora

if dia_hora not in agenda:
    print("No hay ninguna actividad para el día y hora especificados.")
else: 
    print(f"Actividad programada: {agenda[dia_hora]}")

# Ejercicio 10

original = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París",
    "Japón": "Tokio",
    "Canadá": "Ottawa"
}

print(original)

invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print(invertido)