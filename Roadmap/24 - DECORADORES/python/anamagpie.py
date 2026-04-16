'''
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
'''
# Un decorador es una función que 'decora' pero no modifica directamente.

def decorador(funcion):
    def print_funcion():
        print(f"Esta es la función '{funcion.__name__}'.")
        return funcion
    return print_funcion

@decorador
def ejemplo1():
    pass

@decorador
def ejemplo2():
    pass

print("-------------------------------------------------")
print("------------------EJEMPLOS 1 Y 2-----------------")
print("-------------------------------------------------")


ejemplo1()
ejemplo2()

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
'''

def deco_contador(funcion):
    def func_contador():
        func_contador.deco_contador += 1
        print(f"La función '{funcion.__name__}' ha sido ejecutada {func_contador.deco_contador} veces.")
        return funcion

    func_contador.deco_contador = 0
    return func_contador

@deco_contador
def ejemplo3():
    pass

@deco_contador
def ejemplo4():
    pass

print("-------------------------------------------------")
print("--------------------EJEMPLO 3--------------------")
print("-------------------------------------------------")


# Se ejecuta 3 veces
ejemplo3()
ejemplo3()
ejemplo3()


print("-------------------------------------------------")
print("--------------------EJEMPLO 4--------------------")
print("-------------------------------------------------")

#Se ejecuta 7 veces
ejemplo4()
ejemplo4()
ejemplo4()
ejemplo4()
ejemplo4()
ejemplo4()
ejemplo4()
