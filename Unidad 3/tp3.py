# Ejercicio 1

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else: 
    pass

# Ejercicio 2

nota = int(input("Ingrese su nota: "))
print("Aprobado") if nota >= 6 else print("Desaprobado")

# Ejercicio 3

num = int(input("Ingrese un numero par"))

print("Ha ingresado un numero par.") if num % 2 == 0 else print("Por favor, ingrese un nunmero par.")

# Ejercicio 4

edad = int(input("Ingrese su edad: "))

if edad < 12 and edad >= 0: 
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad <= 0:
    print("Por favor, ingrese un numero valido.")
else: 
    print("Adulto/a")

# Ejercicio 5

password = input("Ingrese una contraseña: ")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1,100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if (media > mediana) and (mediana > moda):
    print("Sesgo positivo.")
elif (media < mediana) and (mediana < moda):
    print("Sesgo negativo.")
elif (media == mediana) and (mediana == moda):
    print("Sin sesgo.")
else: 
    pass

# Ejercicio 7

frase = input("Ingrese una frase o palabra: ")

ultima_letra = frase[-1].lower()

if ultima_letra in "aeiou":
    print(frase + "!")
else:
    print(frase)

# Ejercicio 8

nombre = input("Ingrese su nombre: ")
menu = int(input("""Elija una opcion: 
                    1. Transformar a mayúsculas
                    2. Transformar a minúsculas
                    3. Primera letra mayúscula"""))

if menu == 1:
    print(nombre.upper())
elif menu == 2:
    print(nombre.lower())
elif menu == 3:
    print(nombre.title())
else: 
    print("Por favor, elija una opción válida.")

# Ejercicio 9

magnitud = float(input("Escriba la magnitud del terremoto: "))

if magnitud < 3 and magnitud > 0:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7:
    print("Extremo")
else: 
    print("Por favor, ingrese una magnitud válida.")

# Ejercicio 10

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").upper()
mes = input("Ingrese el mes actual: ").lower()
dia = int(input("Ingrese el dia actual: "))

if (mes == "diciembre" and dia >= 21 and dia <= 31) or (mes == "enero" and dia <= 31) or (mes == "febrero" and dia <= 29) or (mes == "marzo" and dia <= 20):
    if hemisferio == 'N':
        print("Invierno")
    else:
        print("Verano")
elif(mes == "marzo" and dia >= 21 and dia <= 31) or (mes == "abril" and dia <= 30) or (mes == "mayo" and dia <= 31) or (mes == "junio" and dia <= 20):
    if hemisferio == 'N':
        print("Primavera")
    else:
        print("Otoño")
elif(mes == "junio" and dia >= 21 and dia <= 30) or (mes == "julio" and dia <= 31) or (mes == "agosto" and dia <= 31) or (mes == "septiembre" and dia <= 20):
    if hemisferio == 'N':
        print("Verano")
    else:
        print("Invierno") 
elif(mes == "septiembre" and dia >= 21 and dia <= 30) or (mes == "octubre" and dia <= 31) or (mes == "noviembre" and dia <= 30) or (mes == "diciembre" and dia <= 20):
    if hemisferio == 'N':
        print("Primavera")
    else:
        print("Otoño")
else:
    print("Ingrese una fecha válida.")