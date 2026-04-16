from functools import reduce
from datetime import datetime

'''
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
'''

#Ejemplo de suma (x + 2) y suma (x + x)

def a_funcion(funcion, x):
    return funcion(x)

print("¿Cuentas letras tiene la palabra 'Cuentaletras'?", a_funcion(len,"Cuentaletras")) # resultado: 12

def suma_n(n):
    def suma (x):
        return x + n
    return suma

suma = suma_n(2)
print("La suma de suma_n(2) + 20 es: ", suma(20))
print("La suma de 8 + 24 es: ", suma_n(8)(24)) # resultado 12/22/32

# Sistema

nums = [3,6,2,7,4]

#map(): Le pasamos una lista y una función. La función se aplica a todos los elementos de la lista.

def sum_dos(n):
    return n + 2

print("Lista original: ", nums)
print("-------------------------------------------------")
print("Map    | Suma 2 a cada número: ", list(map(sum_dos, nums))) # añado list para que imprima

#filter(): Filtra los elementos, muestra solo los True

def pares(n):
    return n % 2 == 0

print("Filter | Números pares de la lista: ", list(filter(pares, nums))) # también añado list

#sorted(): Ordena los elementos

print("Sorted | Números de la lista ASC: ", sorted(nums))
print("Sorted | Números de la lista DESC: ", sorted(nums, reverse=True))
print("Sorted | DESC con key=lambda: ", sorted(nums, key=lambda x: -x))

#reduce(): Acumula valores. Hay que importarlo de functools.

def suma(x, y):
    return x + y

print("Reduce | Suma los números de la lista: ", reduce(suma, nums))


'''
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para 
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
'''
print("-------------------------------------------------")

estudiantes = [ 
    {"nombre" : "Xuacu", "fechanac" : "13-04-2006", "calificaciones" : [7.3, 8.7, 7, 9.1, 6]},
    {"nombre" : "Benito", "fechanac" : "04-02-2006", "calificaciones" : [7, 7, 6.2, 4, 8]},
    {"nombre" : "Marina", "fechanac" : "20-08-2005", "calificaciones" : [5, 5, 5.6, 7, 6.2]},
    {"nombre" : "Lorena", "fechanac" : "16-11-2006", "calificaciones" : [9, 10, 9.5, 9, 9.4]},
    {"nombre" : "Hector", "fechanac" : "08-10-2004", "calificaciones" : [2, 4.2, 3.4, 6, 5.1]}
]

# Media de las calificaciones

def media(calificaciones):
    return sum(calificaciones) / len(calificaciones)

print("Media de las calificaciones de cada estudiante: ")
print(list(map(lambda estudiante: {"nombre": estudiante["nombre"], "media": media(estudiante["calificaciones"])}, estudiantes)))

print("-------------------------------------------------")

# Filtra estudiantes con media mayor o igual que 9: resultado Lorena

def media(calificaciones):
    return sum(calificaciones) / len(calificaciones)

print("Mejor estudiante con media superior a 9: ")
print(list(map(lambda estudiante: estudiante["nombre"], filter(lambda estudiante: media(estudiante["calificaciones"]) >= 9, estudiantes))))

print("-------------------------------------------------")

# Lista segun fechanac DESC / se formatea la fecha con "datetime"

print("Fechas de nacimiento en orden ascendente (empezando por el más joven): ")
print(sorted(estudiantes, key=lambda estudiante: datetime.strptime(estudiante["fechanac"], "%d-%m-%Y"), reverse = True))

print("-------------------------------------------------")

# Calificación más alta de todos los estudiantes: resultado 10

print("Calificación más alta: ")
print(max(map(lambda estudiante: max(estudiante["calificaciones"]), estudiantes)))