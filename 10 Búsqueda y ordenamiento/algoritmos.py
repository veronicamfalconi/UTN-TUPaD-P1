import csv

def cargar_libros(archivo):
    """
    Realiza la carga un archivo CSV con datos de libros.
    Parámetros: archivo (str): Ruta del archivo CSV.
    Retorna: list: Lista de diccionarios con claves: 'titulo', 'autor' y 'puntuacion'.
    """
    # Abrir el archivo CSV en modo lectura con codificación UTF-8
    libros = []
    with open(archivo, newline='', encoding='utf-8') as archivo_csv:
        lector = csv.DictReader(archivo_csv) # Leer filas como diccionarios

        # Convertir cada fila en diccionario con puntuación numérica
        for fila in lector:
            fila["puntuacion"] = float(fila["puntuacion"]) # Convertir a float
            libros.append(fila)
    return libros

def bubble_sort(lista, clave):
    """
    Ordena una lista de diccionarios en orden descendente según el valor asociado a una clave específica.
    Implementa el algoritmo de ordenamiento Bubble Sort (ordenamiento burbuja).

    Parámetros:
    lista --> lista de diccionarios a ordenar
    clave --> clave del diccionario por la cual se realizará el ordenamiento

    Retorna:
    La lista ordenada en orden descendente (modificada en el lugar)
    """
    n = len(lista) # Se obtiene la cantidad de elementos de la lista

    # Bucle externo que recorre la lista
    for i in range(n):
        # Bucle interno para comparar elementos seguidos
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, se intercambian
            if lista[j][clave] < lista[j + 1][clave]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista # Se devuelve la lista ordenada

def selection_sort_desc(lista, clave):
    """
    Ordena una lista de diccionarios en orden descendente según el valor asociado a una clave específica.
    Utiliza el algoritmo de ordenamiento por selección (Selection Sort).

    Parámetros:
    lista --> lista de diccionarios a ordenar
    clave --> clave del diccionario por la cual se realizará el ordenamiento

    Retorna:
    La lista ordenada en orden descendente (modificada en el lugar)
    """
    n = len(lista)  # Se obtiene la longitud de la lista

    # Recorremos todos los elementos de la lista
    for i in range(n):
        # Encontrar el índice del elemento máximo
        max_index = i

        # Comparamos este elemento con todos los demás que siguen en la lista
        for j in range(i + 1, n):
            # Si encontramos un elemento con mayor valor, actualizamos el índice
            if lista[j][clave] > lista[max_index][clave]:
                max_index = j

        # Intercambiamos el elemento actual con el elemento de mayor valor encontrado
        lista[i], lista[max_index] = lista[max_index], lista[i]

    return lista  # Se devuelve la lista ordenada

def insertion_sort_desc(lista, clave):
    """
    Ordena una lista de diccionarios en orden descendente según el valor asociado a una clave específica.
    Utiliza el algoritmo de ordenamiento por inserción (Insertion Sort).

    Parámetros:
    lista: lista de diccionarios a ordenar
    clave: clave del diccionario por la cual se realizará el ordenamiento

    Retorna:
    La lista ordenada en orden descendente (modificada en el lugar)
    """
    # Recorremos la lista desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        actual = lista[i]  # Elemento que se va a insertar
        j = i - 1

        # Mover los elementos que sean menores que el actual a posiciones mayores
        while j >= 0 and lista[j][clave] < actual[clave]:
            lista[j + 1] = lista[j]
            j -= 1

        # Insertamos el elemento en su posición correcta
        lista[j + 1] = actual

    return lista  # Se devuelve la lista ordenada en orden descendente

def quicksort(lista, clave):
    """
    Ordena una lista de diccionarios en orden descendente según el valor de una clave específica.
    Implementa el algoritmo de ordenamiento Quick Sort.

    Parámetros:
    lista --> lista de diccionarios a ordenar (por ejemplo, libros)
    clave --> clave del diccionario por la cual se realizará el ordenamiento (por ejemplo, "puntuacion")

    Retorna:
    Una nueva lista ordenada en orden descendente
    """
    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista
    else:
        # Elegimos el primer elemento como pivote
        pivot = lista[0]

        # Elementos con valor igual o mayor al pivote (para orden descendente)
        greater = [x for x in lista[1:] if x[clave] >= pivot[clave]]

        # Elementos con valor menor al pivote
        less = [x for x in lista[1:] if x[clave] < pivot[clave]]

        # Llamada recursiva: ordenamos las sublistas y unimos todo
        return quicksort(greater, clave) + [pivot] + quicksort(less, clave)

def busqueda_lineal(lista, valor):
    """
    Realiza una búsqueda lineal de libros con una puntuación específica.

    Parámetros:
    lista (list): Lista de libros.
    valor (float): Puntuación a buscar.

    Retorna:
    list: Lista de libros que coinciden con la puntuación.
    """
    resultados = [] # Lista vacía que guarda los libros que cumplan con la condición

    # Recorremos cada libro en la lista
    for libro in lista:
        if libro["puntuacion"] == valor:
            resultados.append(libro) # Lo agregamos a la lista de resultados
    return resultados

def busqueda_binaria(lista, valor):
    """
    Realiza una búsqueda binaria de libros por puntuación en una lista ordenada de forma descendente.

    Importante: la lista debe estar ordenada por puntuación previamente.

    Retorna:
    list: Libros encontrados con la puntuación exacta.
    """
    izquierda = 0 # Límite inferior de la búsqueda
    derecha = len(lista) - 1 # Límite superior de la búsqueda
    resultados = [] # Lista vacía que guarda los libros encontrados

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # Índice del punto medio
        puntuacion_medio = lista[medio]["puntuacion"]  # Se obtiene la puntuación del libro en la posición media

        if puntuacion_medio == valor:
            # Si encuentra una coincidencia, busca alrededor por más resultados iguales
            resultados.append(lista[medio])

            # Buscar hacia la izquierda del centro
            i = medio - 1
            while i >= 0 and lista[i]["puntuacion"] == valor:
                resultados.insert(0, lista[i])  # insertamos al inicio
                i -= 1

            # Buscar hacia la derecha del centro
            i = medio + 1
            while i < len(lista) and lista[i]["puntuacion"] == valor:
                resultados.append(lista[i])  # insertamos al final
                i += 1

            break  # Ya encontramos todas las coincidencias
        elif puntuacion_medio < valor:
            derecha = medio - 1  # Valor está a la izquierda (porque es más alto)
        else:
            izquierda = medio + 1  # Valor está a la derecha (porque es más bajo)

    return resultados  # Devuelve la lista con los libros encontrados (puede estar vacía)