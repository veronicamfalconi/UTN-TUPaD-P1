# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. 

multiplosDeCuatro = list(range(0,100,4))
print(multiplosDeCuatro)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
#  
miLista = ['Colombia', 'Peru', 'Chile', 'Argentina', 'Bolivia']
miLista = miLista[-2:-1]
print(miLista)

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista:
# para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = [] 

listaVacia = []
listaVacia.append('Colombia')
listaVacia.append('Peru')
listaVacia.append('Chile')
print(listaVacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo
# funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"] 

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)

# Respuesta: El programa elimina el número con el valor más alto de la lista. Con remove se elimina un elemento y
# con max(numeros) se selecciona el elemento de mayor valor de la lista.

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos
# primeros.

miLista = list(range(10,31,5))
print(miLista)
miLista = miLista[0:2]
print(miLista)

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["fox","vento"]
print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir
# la lista resultante por pantalla.

dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

dobles1 = []
numeros = [5, 10, 15]
for numero in numeros:
    dobles1.append(2*numero)

print(dobles1)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "fideos"
compras[0].remove("pan")
print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada = [15, "true", [25.5, 57.9, 30.6], "false"]
print(lista_anidada)