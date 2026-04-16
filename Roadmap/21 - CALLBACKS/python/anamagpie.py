import random
import time
import threading

'''
EJERCICIO
Explora el concepto de callback en tu lenguaje creando un ejemplo
simple (a tu elección) que muestre su funcionamiento.

CALLBACK
Función que se pasa a otra función como un argumento,que luego se 
invoca dentro de la función externa para completar algún tipo de 
rutina o acción. Se usa principalmente en "asincronía".
'''

def cargando(porcentaje: int, callback):
    print("Cargando...")
    callback(porcentaje)

def carga_completa(porcentaje: int):
    print(f"Carga completa: {porcentaje}")

cargando("100", carga_completa)

print("________________________________________________________________")

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
'''

# p = pedido
# proceso_p = proceso principal

print("ESTADO DE TU PEDIDO")
print("________________________________________________________________")

def proceso_p(nom_p: str, confirmado_callback, preparado_callback, entregado_callback):
    def proceso():
        confirmado_callback(nom_p)
        time.sleep(random.randint(1,10)) 
        preparado_callback(nom_p)
        time.sleep(random.randint(1,10))
        entregado_callback(nom_p)

    threading.Thread(target=proceso).start() # Salen mensajes aleatoriamente. Varios pedidos a la vez.

def confirmado_p(nom_p: str):
    print(f"¡Encendiendo hornos! Tu {nom_p} ha sido confirmada.")

def preparado_p(nom_p: str):
    print(f"¡Ya queda poco! Tu {nom_p} ya está lista y pronto la tendrás en casa.")

def entregado_p(nom_p: str):
    print(f"¡Entregado! Tu {nom_p} ha sido entregada. ¡Disfruta!")


proceso_p("Pasta Carbonara", confirmado_p, preparado_p, entregado_p)
proceso_p("Lasaña de verduras", confirmado_p, preparado_p, entregado_p)
proceso_p("Ensalada Capresse", confirmado_p, preparado_p, entregado_p)
proceso_p("Pizza Peperonni", confirmado_p, preparado_p, entregado_p)
proceso_p("Burrata con pestos", confirmado_p, preparado_p, entregado_p)
proceso_p("Pizza 4 Quesos", confirmado_p, preparado_p, entregado_p)