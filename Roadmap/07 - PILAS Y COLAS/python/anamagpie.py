'''
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 '''
# Pilas (Last In First Out) - Stack

pila = []

# Push

pila.append("1")
pila.append("2")
pila.append("3")
pila.append("4")
pila.append("5")
print(pila)

# Pop
pila_i = pila[len(pila) - 1]
del pila[len(pila) - 1]
print(pila_i)
print(pila.pop())
print(pila)

# Colas (Firts In Frist Out) - Queue 

#enqueue
cola = []
cola.append(1)
cola.append(2)
cola.append(3)
cola.append(4)
cola.append(5)

#dequeue
print(cola.pop(0)) #El elemento más "antiguo" de la lista: El 1
print(cola)

'''
  * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
'''

# Navegaciín web

def web_nav():

    pila = []

    while True:

        action = input(
            "Añade tu url! Puedes navegar utilizando las palabras: Adelante/Atrás/Salir: "
        )

        if action == "Salir":
            print("Saliendo del navegador web...")
            break
        elif action == "Adelante":
            pass
        elif action == "Atrás":
            if len(pila) > 0:
                pila.pop()
        else:
            pila.append(action)

        if len(pila) > 0:
            print(f"Estás en: {pila[len(pila) - 1]}.")
        else:
            print("Estás en la página de inicio.")


web_nav()


def impresora():

    cola = []

    while True:

        action = input("Introduce los datos que quieras imprimir. Selecciona 'salir' para salir de la aplicación": ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(cola) > 0:
                print(f"Imprimiendo tu mensaje: {cola.pop(0)}")
        else:
            cola.append(action)

        print(f"Cola de impresión: {cola}")


impresora()


