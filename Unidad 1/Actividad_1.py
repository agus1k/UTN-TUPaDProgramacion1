import math

# Ejercicio 1

print("Hola Mundo")

# Ejercicio 2 

nombre = input("Ingrese su nombre: ")

print(f"Hola, {nombre}")

# Ejercicio 3 

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# Ejercicio 4 

radio = int(input("Ingrese el radio de un círculo: "))

area = math.pi * (radio ** 2) 
perimetro = (radio * 2) * math.pi

print(f"El área del círculo es: {area} y el perímetro: {perimetro}")

# Ejercicio 5

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600

print(f"El equivalente en horas es: {horas}")

# Ejercicio 6

numero = int(input("Ingrese un número: "))

print(f"{numero} * 1 = {numero*1} | {numero} * 2 = {numero*2} | {numero} * 3 = {numero*3} | {numero} * 4 = {numero*4}| {numero} * 5 = {numero*5} | {numero} * 6 = {numero*6} | {numero} * 7 = {numero*7} | {numero} * 8 = {numero*8} | {numero} * 9 = {numero*9}")

# Ejercicio 7

numero1 = int(input("Ingrese un numero distinto de 0: "))
numero2 = int(input("Ingrese otro numero distinto de 0: "))

suma = numero1 + numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
resta = numero1 - numero2

print(f"La suma es {suma}, la division {division}, la multiplicacion {multiplicacion} y la resta {resta}")

# Ejercicio 8 

altura = float(input("Ingrese su altura: "))
peso = float (input("Ingrese su peso: "))

imc = peso / (altura) ** 2

print(f"Su indice de masa corporal es: {imc}")

# Ejercicio 9

celsius = int(input("Ingrese una temperatura en grados Celsius"))

farenheit = ((9/5) * celsius) + 32

print(f"El equivalente en Farenheit es: {farenheit}")

# Ejercicio 10

numeroA = int(input("Ingrese un numero: "))
numeroB = int(input("Ingrese un numero: "))
numeroC = int(input("Ingrese un numero: "))

promedio = (numeroA + numeroB + numeroC) / 3

print(f"El promedio es: {promedio}")

