# !!!! IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.

import os

'''
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
'''

nom_txt = "anamagpie.txt"

with open(nom_txt, "w") as file: # Crea el archivo de texto
    file.write("Ana Magpie\n") # Crea lineas en el fichero
    file.write("Python\n")
    file.write("Manejo de ficheros")

with open(nom_txt, "r") as file: # Lee el archivo de texto
    print(file.read()) # Muestra el contenido del txt

os.remove(nom_txt) # Elimina el .txt

print("__________________________________________________")

'''
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
'''

nom_txt = "anamagpie2.txt"

open(nom_txt, "w")

while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Mostrar productos")
    print("6. Consultar ventas totales")
    print("7. Consultar venta por producto")
    print("8. Salir")

    option = input("Selecciona una opcion: ")

    if option == "1":
        nombre = input("Nombre: ")
        cantidad = input("Cantidad: ")
        precio = input("Precio: ")
        with open(nom_txt, "a") as file: # con w sobreescribe y con a(append) añade
            file.write(f"{nombre}, {cantidad}, {precio}\n")
        
    elif option == "2": 
        nombre = input("Nombre: ")
        with open(nom_txt, "r") as file: 
            for line in file.readlines():
                if line.split(", ")[0] == nombre:
                    print(line)
                    break

    elif option == "3":
        nombre = input("Nombre: ")
        cantidad = input("Cantidad: ")
        precio = input("Precio: ")
        with open(nom_txt, "r") as file: # lee el fichero antes de escribir
            lines = file.readlines() 
        with open(nom_txt, "w") as file:
            for line in lines:
                if line.split(", ")[0] == nombre:
                    file.write(f"{nombre}, {cantidad}, {precio}\n")
                else:
                    file.write(line)

    elif option == "4":
        nombre = input("Nombre: ")
        with open(nom_txt, "r") as file: # lee el fichero antes
            lines = file.readlines()
        with open(nom_txt, "w") as file:
            for line in lines:
                if line.split(", ")[0] != nombre: # mismo código que en la opción 3 pero uso !=
                    file.write(line)

    elif option == "5":
        with open(nom_txt, "r") as file:
            print(file.read())

    elif option == "6":
        total = 0
        with open(nom_txt, "r") as file:
            for line in file.readlines():
                items = line.split(", ")
                cantidad = int(items[1])
                precio = float(items[2])
                total += cantidad * precio
        print(total)

    elif option == "7":
        nombre = input("Nombre: ")
        total = 0
        with open(nom_txt, "r") as file:
            for line in file.readlines():
                items = line.split(", ")
                if items[0] == nombre:
                    cantidad = int(items[1])
                    precio = float(items[2])
                    total += cantidad * precio
                    break
        print(total)

    elif option == "8":
       os.remove(nom_txt)
    break

else:
    print("Selecciona una opción.")