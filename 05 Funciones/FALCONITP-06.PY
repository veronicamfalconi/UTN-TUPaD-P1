# # 1. Crear una función llamada imprimir_hola_mundo que imprima por
# # pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# # programa principal.

# #funciones
# def saludar(mensaje):
#     print("Hola mundo!")
# #programa principal
# saludar("Hola mundo")

# # 2. Crear una función llamada saludar_usuario(nombre) que reciba
# # como parámetro un nombre y devuelva un saludo personalizado.
# # Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# # principal solicitando el nombre al usuario.

# #funciones
# def saludar_usuario(nombre):
#     print(f"Hola {nombre}!")
# #programa principal
# saludar_usuario("Marcos")

# # 3. Crear una función llamada informacion_personal(nombre, apellido,
# # edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# # [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario 
# # y llamar a esta función con los valores ingresados.

# #funciones
# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# #programa principal
# nombre = input("Ingrese su nombre")
# apellido = input("Ingrese su apellido")
# edad = int(input("Ingrese su edad"))
# residencia = input("Ingrese su residencia")

# informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro
# y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio 
# como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y 
# llamar ambas funciones para mostrar los resultados.

#funciones
# def calcular_area_circulo(numero):
#     area = 3,14 * numero**2
#     print(f"{area}")

# def calcular_perimetro_circulo(numero):
#     perimetro = 2 * 3,14 * numero
#     print(f"{perimetro}")

# #programa principal
# radio = int(input("Ingrese el radio del circulo"))
# calcular_area_circulo(radio)
# calcular_perimetro_circulo(radio)

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#funciones
# def validar_entero(mensaje, min = float("-inf"), max = float("inf")):
#     n = int(input(f"{mensaje}"))
#     while n < min or n > max:
#         n = int(input(f"ERROR, {mensaje}"))
#     return n

# def segundos_a_minutos(segundos):
#     minutos = segundos // 60
#     return minutos

# def segundos_a_horas(segundos):
#     horas = segundos // 3600
#     if segundos % 3600 != 0 or segundos < 3600:
#         segundos_restantes = segundos % 3600
#     minutos = segundos_a_minutos(segundos_restantes)
#     return horas, minutos

# #programa principal
# segundos = validar_entero("Ingrese los segundos: ", 0)
# horas, minutos = segundos_a_horas(segundos)
# print(f"{segundos} segundos es/son {horas} hora/s y {minutos} minutos")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

#funciones
# def validar_entero(mensaje, min = float("-inf"), max = float("inf")):
#     n = int(input(f"{mensaje}"))
#     while n < min or n > max:
#         n = int(input(f"ERROR, {mensaje}"))
#     return n

# def tabla_multiplicar(numero):
#     for i in range(1,11):
#         producto = numero * i
#         print(f"{numero} x {i} = {producto}")

# #programa principal
# num = validar_entero("Ingrese un número entero: ", 1)
# tabla_multiplicar(num)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado 
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

#funciones
# def validar_numero(mensaje, min = float("-inf"), max = float("inf")):
#     n = int(input(f"{mensaje}"))
#     while n < min or n > max:
#         n = int(input(f"ERROR, {mensaje}"))
#     return n

# def operaciones_basicas(a, b):
#     sumar = a + b
#     restar = a - b
#     multiplicar = a * b
#     if a < b:
#         dividir = b // a
#     else:
#         dividir = a // b
#     return(sumar, restar, multiplicar, dividir)

# #programa principal
# num1 = validar_numero("Ingrese un número: ")
# num2 = validar_numero("Ingrese otro número: ")
# resultados = operaciones_basicas(num1, num2)
# suma = print(f"La suma de {num1} y {num2} es {resultados[0]}")
# resta = print(f"La resta de {num1} y {num2} es {resultados[1]}")
# producto = print(f"El producto de {num1} y {num2} es {resultados[2]}")
# division = print(f"La división entre {num1} y {num2} es {resultados[3]}")


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función 
# para mostrar el resultado con dos decimales.

#funciones
# def validar_float(mensaje, n, min = float("-inf"), max = float("inf")):
#     n = float(input(f"{mensaje}"))
#     while n < min or n > max:
#         n = float(input(f"ERROR, {mensaje}"))
#     return n

# def validar_entero(mensaje, n, min = float("-inf"), max = float("inf")):
#     n = int(input(f"{mensaje}"))
#     while n < min or n > max:
#         n = float(input(f"ERROR, {mensaje}"))
#     return n

# def calcular_imc(peso, altura, decimales):
#     imc = (peso**2) / altura
#     return round(imc, decimales)

# #programa principal
# peso = validar_float("Ingrese su peso en kilogramos: ", 1)
# altura = validar_entero("Ingrese su altura en metros: ", 1)
# imc = calcular_imc(peso, altura, 2)
# print(f"El IMC es {imc}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

#funciones
# def validar_float(mensaje, min = float("-inf"), max = float("inf")):
#     n = float(input(f"{mensaje}"))
#     while n < min or n > max:
#         n = float(input(f"ERROR, {mensaje}"))
#     return n

# def celsius_a_fahrenheit(celsius, decimales):
#     fahrenheit = celsius * 9 / 5 + 32
#     return round(fahrenheit, decimales)

# #programa principal
# temperatura = validar_float("Ingrese la temperatura: ")
# temperaturaEnF = celsius_a_fahrenheit(temperatura, 2)
# print(f"La temperatura de {temperatura}°C equivale a {temperaturaEnF}°F")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

#funciones
def validar_entero(mensaje, min = float("-inf"), max = float("inf")):
    n = int(input(f"{mensaje}"))
    while n < min or n > max:
        n = float(input(f"ERROR, {mensaje}"))
    return n

def calcular_promedio(a, b, c, decimales):
    promedio = (a + b + c) / 3
    return round(promedio, decimales)

#programa principal
num1 = validar_entero("Ingrese un numero: ")
num2 = validar_entero("Ingrese otro numero: ")
num3 = validar_entero("Ingrese un numero más: ")
promedio = calcular_promedio(num1, num2, num3, 2)
print(f"El promedio entre {num1}, {num2} y {num3} es {promedio}")

