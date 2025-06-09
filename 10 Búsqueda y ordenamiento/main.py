import timeit
from algoritmos import cargar_libros, bubble_sort, selection_sort_desc, insertion_sort_desc, busqueda_lineal, busqueda_binaria, quicksort, medir_tiempo
import os
print("Directorio actual:", os.getcwd())

# Cargar libros desde el archivo
directorio_actual = os.path.dirname(__file__)
ruta_archivo = os.path.join(directorio_actual, "libros-famosos.csv")
libros = cargar_libros(ruta_archivo)

# Elegir una puntuación objetivo
objetivo = 5.0

# Medir ordenamiento
# Bubble Sort
libros_bubble = libros.copy()
start_bubble = timeit.default_timer()
ordenados_bubble = bubble_sort(libros_bubble, "puntuacion")
end_bubble = timeit.default_timer()
print(f"Bubble Sort: Tiempo = {end_bubble - start_bubble:.6f} segundos")

# Selection Sort
libros_selection = libros.copy()
start_selection = timeit.default_timer()
ordenados_selection = selection_sort_desc(libros_selection, "puntuacion")
end_selection = timeit.default_timer()
print(f"Selection Sort: Tiempo = {end_selection - start_selection:.6f} segundos")

# Insertion Sort
libros_insertion = libros.copy()
start_insertion = timeit.default_timer()
ordenados_insertion = insertion_sort_desc(libros_insertion, "puntuacion")
end_insertion = timeit.default_timer()
print(f"Insertion Sort: Tiempo = {end_insertion - start_insertion:.6f} segundos")

# Quick Sort
start = timeit.default_timer()
ordenados_quick = quicksort(libros.copy(), "puntuacion")
end = timeit.default_timer()

print(f"Quick Sort: Tiempo = {end - start:.6f} segundos")

#Medir búsqueda
# Búsqueda lineal sobre la lista ordenada con bubble_sort
start_busqueda = timeit.default_timer()
resultados = busqueda_lineal(ordenados_bubble, objetivo)
end_busqueda = timeit.default_timer()
print(f"Búsqueda Lineal: Resultados = {len(resultados)}, Tiempo = {end_busqueda - start_busqueda:.6f} segundos")

# Búsqueda binaria sobre lista ordenada (bubble sort)
start_binaria = timeit.default_timer()
resultado_binaria = busqueda_binaria(ordenados_bubble, objetivo)
end_binaria = timeit.default_timer()
if resultado_binaria:
    print(f"Búsqueda Binaria: Resultados = {len(resultado_binaria)}, Tiempo = {end_binaria - start_binaria:.6f} segundos")
else:
    print(f"Búsqueda Binaria: No encontrado, Tiempo = {end_binaria - start_binaria:.6f} segundos")