import random

# Ejercicio 1

for i in range(101):
    print(i)

# Ejercicio 2

num = int(input("Ingrese un número entero: "))
i = 0

num = abs(num)

if num == 0:
    i = 1
else: 
    while num > 1:
        num //= 10
        i += 1

print(f"El número tiene {i} dígitos")

# Ejercicio 3

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
total = 0

menor = min(num1, num2)
mayor = max(num1, num2)

for i in range(menor + 1, mayor):
    total += i

print(f"El total es: {total}")

# Ejercicio 4

num = 1
total = 0

while num != 0:
    num = int(input("Ingrese un número (0 para salir):" ))
    total += num
    
print(f"El total es: {total}")

# Ejercicio 5

num = random.randint(0, 9)
userNum = -1
i = 0

while userNum != num:
    i += 1
    userNum = int(input("Adivina el número entre 0 y 9: "))

print(f"Acertaste en {i} intentos. El número era: {num}")

# Ejercicio 6

for i in range(100, 0, -2):
    print(i)

# Ejercicio 7 

num = int(input("Ingrese un número positivo: "))
total = 0

for i in range(0, num + 1):
    total += i

print(f"El total es {total}")

# Ejercicio 8

contPar = 0
contImpar = 0 
contNeg = 0 
contPos = 0
num = 0

for i in range(100):
    num = int(input("Ingrese un número: "))

    if num % 2 == 0:
        contPar += 1
    else:
        contImpar += 1

    if num > 0:
        contPos += 1
    elif num < 0: 
        contNeg += 1

print(f"Hay {contPar} números pares, {contImpar} números impares, {contPos} números positivos y {contNeg} números negativos.")

# Ejercicio 9

total = 0

for i in range(100):
    num = int(input("Ingrese un número: "))

    total += num

promedio = total / 100

print(f"El promedio es: {promedio}")

# Ejercicio 10

num = int(input("Ingrese un número para invertir: "))

numInvertido = 0

while num > 0:
    digito = num % 10
    numInvertido = numInvertido * 10 + digito
    num //= 10

print(f"El número invertido es: {numInvertido}")










