# 1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'], precios_frutas['Manzana'], precios_frutas['Pera'] = 1200, 1500, 2300

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800 

precios_frutas['Banana'], precios_frutas['Manzana'], precios_frutas['Melón'] = 1330, 1700, 2800
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
#  crear una lista que contenga únicamente las frutas sin los precios. 

precios = list(precios_frutas.values())
print(precios)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe. Ejemplo:

numero_telefono = {}

def agregar_contacto(diccionario):
    clave = input("Ingrese un nombre: ")
    valor = int(input("Ingrese un teléfono"))
    diccionario[clave] = valor
    return diccionario

while len(numero_telefono) < 5:
    agregar_contacto(numero_telefono)

print(numero_telefono)

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra. Ejemplo: 

def pedir_ingreso():
    ingreso = input("Ingrese una frase: ")
    return ingreso

def solo_palabra(ingreso):
    palabras = ingreso.split()
    return palabras

def ingreso_set(palabras):
    palabras_set = set(palabras)
    return palabras_set

frase = pedir_ingreso()
palabras_unicas = ingreso_set(solo_palabra(frase))
print(palabras_unicas)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.
#  Ejemplo: 

dicc = {}
dicc2 = {}

def pedir_ingreso(frase):
    ingreso = input(f"Ingrese un {frase}: ")
    return ingreso

while len(dicc) < 3:
    nombre = pedir_ingreso("nombre")
    lista_nota = []
    for i in range(3):
        nota = int(pedir_ingreso(f"nota {i+1}"))
        lista_nota.append(nota)
    dicc[nombre] = tuple(lista_nota)

for nombre, tupla in dicc.items():
    promedio = sum(tupla) / len(tupla)
    dicc2[nombre] = promedio

print(dicc)

for nombre, promedio in dicc2.items():
    print(f"El promedio de {nombre} es {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

parcial1 = {'Sol', 'Pepe', 'Rosa', 'Pedro', 'María', 'Eva'}
parcial2 = {'Juan', 'Rosa', 'Jose', 'Sol', 'María'}

ambos = parcial1 & parcial2
print(f"Aprobados en ambos parciales ", ambos)

solo_uno = parcial1 ^ parcial2
print(f"Aprobados solo uno ", solo_uno)

al_menos_uno = parcial1 | parcial2
print(f"Aprobados al menos uno ", al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe. 

dicc = {
    'Cuadernos': 1200,
    'Lapiceras': 2000,
    'Pinceles': 1500
}
opcion = ""

while opcion != 4:
    print("\n--- MENÚ ---")
    print("\n1. Consultar el stock de un producto ingresado")
    print("\n2.Agregar unidades al stock si el producto ya existe")
    print("\n3.Agregar un nuevo producto si no existe")
    print("\n4.Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        producto = input("Ingrese el producto para consultar el stock: ")
        if producto in dicc:
            print(f"El stock de {producto} es {dicc[producto]}")
        else:
            print(f"No existe el producto indicado")
    elif opcion == 2:
        producto = input("Ingrese el producto para agregar al stock: ")
        if producto in dicc:
            stock = int(input("Ingrese la cantidad que desea agregar: "))
            dicc[producto] += stock
            print(f"El nuevo stock de {producto} es {dicc[producto]}")
        else:
            print("No existe el producto ingresado.")
    elif opcion == 3:
        productoNuevo = input("Ingrese el nuevo producto: ")
        if productoNuevo not in dicc:
            stockNuevo = int(input(f"Ingrese el stock para {productoNuevo}: "))
            print(f"El stock de {productoNuevo} es de {stockNuevo}")
    else:
        print("\nOpción ivalida, ingrese una opción: ")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
# Permití consultar qué actividad hay en cierto día y hora. 

agenda = {
    ('Lunes', 19): 'Salsa',
    ('Martes', 18): 'Inglés',
    ('Miercoles', 10): 'Dentista',
    ('Jueves', 12): 'Reunión'
}
print(agenda)
dia = input("Ingrese el día: ")
hora = int(input("Ingrese la hora: "))
clave = (dia, hora)
if clave in agenda:
    print(f"El {dia} a las {hora} tiene un evento para: {agenda[clave]}")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores. Ejemplo:

capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "México": "Ciudad de México",
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín",
    "Japón": "Tokio"
}

paises = {}

for pais, capital in capitales.items():
    paises[capital] = pais

print(paises)