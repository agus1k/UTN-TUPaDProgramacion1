# NOTA IMPORTANTE:
# Al crear el archivo inicial productos.txt, cada línea debe terminar con un salto de línea (\n),
# incluso la última, sino se produce un error.
# Existen métodos para verificar si tiene salto de línea o no y agregarlo, pero como todavía no vimos ese tema, decidí simplemente aclararlo acá.

# Paso 2

def leer_productos():
    with open("productos.txt", "r") as productos:
        for linea in productos:
            nombre, precio, cantidad = linea.strip().split(",")

            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# Paso 3

def agregar_producto():
    while True:
        print("Ingrese un nuevo producto: ")
        nombre = input("Nombre: ")
        precio = input("Precio: ")
        cantidad = input("Cantidad: ")

        with open("productos.txt", "a") as productos:
            productos.write(f"{nombre},{precio},{cantidad}\n") 

        opcion = input("Desea agregar otro producto?: ").strip().lower()

        if opcion != 's':
            break

# Paso 4

def cargar_productos():
    productos = []

    with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                producto = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad":int(cantidad)
                }
                productos.append(producto)
    return productos

# Paso 5

def buscar_producto(productos):
    nombre_buscar = input("Ingrese el nombre del producto que desea buscar: ")

    encontrado = False
    for p in productos:
        if p["nombre"].lower() == nombre_buscar.lower():
            print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
            encontrado = True
            break

    if not encontrado:
        print("El producto no existe en la lista.")

# Paso 6
def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

    print("Archivo actualizado.")

leer_productos()
agregar_producto()
leer_productos()

productos = cargar_productos()

for p in productos:
    print(p)

buscar_producto(productos)
guardar_productos(productos)
     

