'''
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
'''

# EXCEPCIONES

try:
    print(10/0)
    print("Funciona!")

except:
    print("Error inesperado. ¡Menos mal que puse try/except!")

print("Continua ejecutando el resto sin problema, pero si le meto 'Exception as e'...")

try:
    print(10/2)

    lista = [1, 2, 3, 4]
    print(lista[7])

except Exception as e:
    print(f"Error intesperado: {e}")

print("Me chiva el error :)")


'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.  
'''

print("_____________________________________")
print("Ejercicio Extra:")

class ErrorInvent(Exception):
    pass

def procesar_params(parametros: list):

    if len(parametros) < 3:
        raise  IndexError()
    elif parametros[1] == 0:
        raise ZeroDivisionError()
    elif type(parametros[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una string.")
        

    print(parametros[2])
    print(parametros[0]/parametros[1])
    print(parametros[2] + 7)


try:
    procesar_params([1, 2, 3, 4])

except IndexError as e:
    print(f"Error inesperado: El número de elementos debe ser mayor que 2.")
except ZeroDivisionError as e:
    print("El segundo elemento no puede ser 0.")
except Exception as e:
    print(f"Error inesperado: {e}")

else:
    print("No se han producido errores.")
finally:
    print("El programa funciona correctamente.")