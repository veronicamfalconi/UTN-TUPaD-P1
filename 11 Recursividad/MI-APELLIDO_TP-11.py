# 1)Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y 
# mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

#funciones
def numeroPedido():
    num = int(input("Ingrese un número: "))
    return num
    
def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)

#programa principal
for i in range(1,numeroPedido()+1):
    print(f"El factorial de {i} es {factorial(i)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, 
# muestra la serie completa hasta la posición que el usuario especifique.
#funciones
def numeroPedido():
    num = int(input("Ingrese un número: "))
    return num
    
def serieFibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return posicion + serieFibonacci(posicion-1) + serieFibonacci(posicion-2)

#programa principal
for i in range(numeroPedido()):
    print(f"En la posición {i} obtenemos el valor de Fibonnacci: {serieFibonacci(i)}")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula
#  𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.
#funciones
def numeroPedido(mensaje):
    num = int(input(mensaje))
    return num

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base*potencia(base, exponente-1)

#programa principal
base = numeroPedido("Ingrese la base: ")
exponente = numeroPedido("Ingrese el exponente: ")
print(f"El resultado de elevar {base} a la {exponente} es igual a {potencia(base, exponente)}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación
#  en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. Para convertir
#  un número decimal a binario, se puede seguir este procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

#funciones
def numeroPedido(mensaje):
    num = int(input(mensaje))
    return num

def decimalBinario(decimal):
    if (decimal < 2):
        return str(decimal)
    else:
        return decimalBinario(decimal // 2) + str(decimal % 2)
    
#programa principal
decimal = numeroPedido("Ingrese un número decimal")
print(f"El número decimal {decimal} en binario es {decimalBinario(decimal)}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes,
#  y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().
#funciones
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

#programa principal
palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print(f"{palabra} es un palindromo")
else:
    print(f"{palabra} no es un palindromo")
# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma 
# de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)
#funciones
def numeroPedido(mensaje):
    num = int(input(mensaje))
    return num

def suma_digitos(n):
    if n < 10:
        return n % 10
    else:
        return suma_digitos(n // 10) + (n%10)

#programa principal
numeroIngresado = numeroPedido("Ingrese un número: ")
print(f"La suma de los dígitos de {numeroIngresado} es {suma_digitos(numeroIngresado)}")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, 
# en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva 
# el total de bloques que necesita para construir toda la pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)
#funciones
def numeroPedido(mensaje):
    num = int(input(mensaje))
    return num

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)
    
#programa principal
numeroBloques = numeroPedido("Ingrese la cantidad de ladrillos de la base: ")
print(f"La cantidad de ladrillos que se necesitan para construir la piramide con un base de {numeroBloques} es {contar_bloques(numeroBloques)}")
# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) 
# y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0
#funciones
def numeroPedido(mensaje):
    num = int(input(mensaje))
    return num

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    resto = numero // 10
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)
        
#programa principal
numero1 = numeroPedido("Ingrese un número: ")
digito1 = numeroPedido("Ingrese un dígito entre 0 y 9: ")

print(f"El dígito {digito1} aparece en el número {numero1} {contar_digito(numero1, digito1)} veces")
