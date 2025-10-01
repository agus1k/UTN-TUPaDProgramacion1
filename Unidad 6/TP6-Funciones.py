
import math

# Ejercicio 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# Ejercicio 2

def saludar_usuario(nombre):
    return (f"Hola {nombre}!")

print(saludar_usuario(input("Por favor, ingrese su nombre: ")))

# Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4

def calcular_area_circulo(radio):
     return math.pi * math.pow(radio, 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio: "))

print(f"Area: {calcular_area_circulo(radio)}")
print(f"Perimetro: {calcular_perimetro_circulo(radio)}")

# Ejercicio 5

def segundos_a_horas(segundos):
    return segundos / 3600

seg = int(input('Ingrese la cantidad de segundos: '))
print(f"Equivalente en horas: {segundos_a_horas(seg)}")

# Ejercicio 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero * i)

num = int(input("Ingrese un número: "))
tabla_multiplicar(num)

# Ejercicio 7

def operaciones_basicas(a, b):
    if b == 0:
        return (a + b, a - b, a * b, "Error: división por cero")
    return (a + b, a - b, a * b, a / b)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(num1,num2)

print(f"Suma:  {resultados[0]}")
print(f"Resta:  {resultados[1]}")
print(f"Multiplicación:  {resultados[2]}")
print(f"División:  {resultados[3]}")

# Ejercicio 8

def calcular_imc(peso, altura):
    return peso / math.pow(altura, 2)

peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))

print(f"{calcular_imc(peso, altura):.2f}")

# Ejercicio 9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese los grados en celsius: "))
print(f"{celsius_a_fahrenheit(celsius)}")

# Ejercicio 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

print(f"PromedioL {calcular_promedio(a, b, c)}")



