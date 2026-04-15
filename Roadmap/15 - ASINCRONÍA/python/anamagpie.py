import datetime
import time
import asyncio #asíncrono

'''
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
'''

async def tarea(nombre: str, duracion: int): # añado async
    print(
        f"Tarea: {nombre}. Duración: {duracion}s. Inicio: {datetime.datetime.now()}")
    #time.sleep(duracion)
    await asyncio.sleep(duracion)
    print(
        f"Tarea: {nombre}. Fin: {datetime.datetime.now()}")

asyncio.run(tarea("1 - Contar dos segundos", 2)) # añado asyncio.run()

'''
 * DIFICULTAD EXTRA:
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
'''

async def async_tareas():
    await asyncio.gather(tarea("C - Contar tres segundos", 3), tarea("B - Contar dos segundos", 2), tarea("A - Contar un segundo", 1))
    await tarea("D - Contar un segundo", 1)

asyncio.run(async_tareas())