from math import trunc
import random

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = int(input("Ingrese un número entero: "))
cantDigitos = 0
numeroTruncado = num

while numeroTruncado > 0:
    numeroTruncado = trunc(numeroTruncado/10)
    cantDigitos += 1
    
print(f"La cantidad de dígitos que tiene {num} es {cantDigitos}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

sumatoria = 0
numeroUno = int(input("Ingrese el primer número: "))
numeroDos = int(input("Ingrese el segundo número: "))

if numeroUno < numeroDos:
    limiteMenor = numeroUno
    limiteMayor = numeroDos
else:
    limiteMenor = numeroDos
    limiteMayor = numeroUno

if limiteMenor == limiteMayor or limiteMayor == (limiteMenor + 1):
    print("Ha ingresado dos números iguales o consecutivos, debe ingresar dos números diferentes y no consecutivos")
else:
    for i in range(limiteMenor + 1, limiteMayor):
        sumatoria += i

print(f"La suma de los números entre {limiteMenor} y {limiteMayor} es {sumatoria}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

CORTE = 0 
sumatoria = 0
num = None #inicializo el num para que entre al while

while num != CORTE:
    num = int(input("Ingrese un número entero o presione 0 para salir: "))
    sumatoria += num #sumatoria en secuencia

if sumatoria == 0:
    print("No se han ingresado números")
else:
    print(f"El total acumulado es: {sumatoria}") #muestro el total

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

numeroAleatorio = random.randint(0, 9)
contador = 1

numeroIngresado = int(input(f"Intento N°{contador}. Ingrese un número entre 0 y 9: "))

while numeroIngresado != numeroAleatorio:
    contador += 1
    numeroIngresado = int(input(f"Intento N°{contador}. Ingrese un número entre 0 y 9: "))
    

print(f"Número acertado! Cantidad de intentos {contador}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, 0, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario

numLimite = int(input("Ingrese un número: "))
suma = 0

for i in range(0, numLimite + 1):
    suma += i

print(f"La suma de los numeros entre 0 y {numLimite} es {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

contNumeros = 0
cantPar = 0
cantImpar = 0
cantNegativos = 0
cantPositivos = 0
cantCero = 0

while contNumeros < 100:
    contNumeros += 1
    num = int(input(f"Ingrese número {contNumeros}: "))
    if num % 2 == 0:
        cantPar += 1
    else:
        cantImpar += 1
    if num > 0:
        cantPositivos += 1
    elif num < 0:
        cantNegativos += 1
    else: 
        cantCero += 1

print(f"La cantidad de números pares es {cantPar}\n")
print(f"La cantidad de números impares es {cantImpar}\n")
print(f"La cantidad de números positivos es {cantPositivos}\n")
print(f"La cantidad de números negativos es {cantNegativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

contador = 0
sumatoria = 0

while contador < 10:
    contador += 1
    num = int(input(f"Ingrese número {contador}: "))
    sumatoria += num

media = sumatoria / contador
print(f"La media de los números ingresados es {media}")
    

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número: "))
numTruncado = num
numInvertido = 0

while numTruncado > 0:
    digito = numTruncado % 10
    numInvertido = (numInvertido*10) + digito
    numTruncado //= 10
    
print(f"El inverso del número {num} es {numInvertido}")