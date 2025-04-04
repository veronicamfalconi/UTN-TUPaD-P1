from statistics import mode, median, mean
import random

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

limite = 18
edad = input("Bienvenida/o. Ingrese su edad: ")
edad = int(edad)
if edad > limite:
    print("Es mmayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

notaLimite = 6
notaUsuario = input("Ingrese su nota: ")
notaUsuario = float(notaUsuario)
if notaUsuario >= notaLimite:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

numeroIngresado = input("Ingrese un número par")
numeroIngresado = int(numeroIngresado)
if numeroIngresado % 2 == 0: 
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edadUsuario = input("Ingrese su edad: ")
edadUsuario = int(edadUsuario)
if edadUsuario < 12:
    print("Categoría niño/a");
elif edadUsuario < 18:
    print("Categoría adolescente");
elif edadUsuario < 30:
    print("Categoría adulto/a jóven");
else:
    print("Categoría Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

contraseña = input("Ingrese su contraseña de longitud entre 8 y 14 caracteres")
longitudContraseña = len(contraseña)
if longitudContraseña >= 8 and longitudContraseña <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positívo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana and media == moda:
    print("sin sesgo")
else:
    print("No se puede determinar el sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

palabraIngresada = input("Ingrese una palabra o frase: ")
ultimaLetra = palabraIngresada[-1]
if ultimaLetra == 'a' or ultimaLetra == 'e' or ultimaLetra == 'i' or ultimaLetra == 'o' or ultimaLetra == 'u':
    print(f"{palabraIngresada}!")
else:
    print(f"{palabraIngresada}")

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombreIngresado = input("Ingrese su nombre: ")
opcionIngresada = input("Ingrese una opción:\n1. Si quiere su nombre en mayúsculas.\n2. Si quiere su nombre en minúsculas.\n3. Si quiere su nombre con la primera letra mayúscula. ")
opcionIngresada = int(opcionIngresada)
if opcionIngresada == 1:
    print(nombreIngresado.upper())
elif opcionIngresada == 2:
    print(nombreIngresado.lower())
elif opcionIngresada == 3:
    print(nombreIngresado.title())
else:
    print("Ingrese una opción válida")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

magnitudTerremoto = input("Ingrese la mágnitud del terremoto: ")
magnitudTerremoto = float(magnitudTerremoto)
if magnitudTerremoto < 3:
    print("Muy leve (imperceptible)")
elif magnitudTerremoto < 4:
    print("Leve (ligeramente perceptible)") 
elif magnitudTerremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitudTerremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitudTerremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")
