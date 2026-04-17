
'''
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
'''
# Recursividad // Función que se llama a ella misma // Parecido a bucle for.

def cuenta_atras(num: int):
    if num >= 0:
        print(num)
        cuenta_atras(num -1) #Para en 0. Evito que entre en bucle infitnito!!!

cuenta_atras(100) #Cuenta desde 100

'''
 * DIFICULTAD EXTRA:
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 '''

#Factorial

def factorial(num: int) -> int:
    if num < 0:
        return 0
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(4))

#Fibonacci

def fibonacci(num: int) -> int:
    if num <= 0:
        print("Número no válido")
        return 0
    elif num == 1:
        return 0
    elif num == 2:
        return 1 #Hasta aquí: números que todavía no se pueden calcular
    else: 
        return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(7)) 







