# Ejercicio 1

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
num_usuario = int(input("Ingrese un número entero positivo: "))

if num_usuario < 1:
    print("Ingrese un número mayor o igual a 1")
else:
    for i in range(1, num_usuario + 1):
        print(factorial(i))

# Ejercicio 2

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    
    return fibonacci(pos-1) + fibonacci(pos-2)

num_usuario = int(input("Ingrese un número entero positivo: "))

if num_usuario < 1:
    print("Ingrese un número mayor o igual a 1")
else:
    for i in range(1, num_usuario + 1):
        print(fibonacci(i))

# Ejercicio 3

def potencia(n,m):
    if m == 0:
        return 1
    else:
        return n * potencia(n,m-1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

print(f"{base} elevado a la {exponente} es {potencia(base, exponente)}")

# Ejercicio 4

def calcular_binario(num):
    if num < 2:
        return str(num)
    else:
        resto = num % 2
        cociente = num // 2

        return calcular_binario(cociente) + str(resto)
    
num_usuario = int(input("Ingrese un número entero positivo: "))

print(f"El número {num_usuario} en binario es: {calcular_binario(num_usuario)}")

# Ejercicio 5

def es_palindromo(palabra):
    if len(palabra) == 0 or len(palabra) == 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False

palabra = input("Ingrese una palabra: ")
print(es_palindromo(palabra))

# Ejercicio 6

def suma_digitos(n):
    
    if n < 1:
        return 0
    else:
        digito = n % 10
        return digito + suma_digitos(n // 10)

n = int(input("Ingrese un numero: "))
print(suma_digitos(n))

# Ejercicio 7

def contar_bloques(n):
    if n == 1:
        return 1
    else: 
        return n + contar_bloques(n-1)

cant_bloques = int(input("Ingrese la cantidad de bloques del primer nivel: "))
print(f"El total de bloques necesarios es: {contar_bloques(cant_bloques)}")

# Ejercicio 8

def contar_digito(numero, digito):

    if numero < 1:
        return 0

    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10,digito)
    else:
        return 0 + contar_digito(numero // 10,digito)
    
numero = int(input("Ingrese un numero: "))
digito = int(input("Ingrese el digito que desea buscar (entre 0 y 9): "))

print(f"El numero {digito} aparece {contar_digito(numero,digito)} veces en {numero}")




    
            




