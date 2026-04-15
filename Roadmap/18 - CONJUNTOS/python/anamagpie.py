'''
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
'''

data = [1, 2, 3, 4, 5]
print("Lista original: ", data)

data.append(6)
print("Añade un elemento al final con append (6): ", data)

data.insert(0, 0)
print("Añade un elemento al principio con instert (0): ", data)

data.extend([7, 8, 9, 10])
print("Añade 7, 8, 9 y 10 con extend: ", data)

data[5:5] = [80, 90]
print("Añade 80 y 90 a  partir de la quinta posición de la lista con slice: ", data)

del data[5]
print("Borra el 80 con de", data)

data[7] = -1
print("Actualiza el 7 con [7]:", data)

print(f"Comprueba si -5 existe: False: {-5 in data}")
print(f"Comprueba si 5 existe: True: {5 in data}")

data.clear() #limpia el contenido de data != del data!!!
print("Borra el contenido de data: ", data)

'''
 * DIFICULTAD EXTRA:
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
'''

set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3, 4, 7, 8, 10, 13}

print("Sets Originales: Set 1 ->", set_1, "Set 2 ->", set_2)
print(f"Unión de conjuntos: {set_1.union(set_2)}")
print(f"Intersección de conjuntos: {set_1.intersection(set_2)}") # Lo que comparten
print(f"Diferencia: {set_1.difference(set_2)}") # El unico elemento ÚNICO que pertenece a set 1
print(f"Diferencia simétrica: {set_1.symmetric_difference(set_2)}") # Todo lo que no tienen en común | Contrario a intersección