'''
EJERCICIO:
 - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
   su tipo de dato.
 - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
    (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 '''

# --- Tipos de datos

# Por valor // 

entero_a = 5
entero_b = entero_a
entero_b = 10
print(entero_a)
print(entero_b)

# Por referencia // Se almacenan dentro de la misma posición de memoria. Se modifica la variable original.

entero_a = [5, 10]
entero_b = entero_a
entero_b.append(15)
print(entero_a)
print(entero_b)


# Funciones: Por valor

entero_c = 10

def entero_func(entero: int):
    entero = 20
    print(entero)


entero_func(entero_c)
print(entero_c)

# Funciones con datos por referencia

def lista_func(lista: list):
    lista.append(15)

    lista_d = lista
    lista_d.append(20)

    print(lista)
    print(lista_d)

lista_c = [5, 10]
lista_func(lista_c)
print(lista_c)


'''
  * DIFICULTAD EXTRA:
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 '''

# Por valor

def por_valor(valor_a: int, valor_b: int) -> tuple:
    temp = valor_a
    valor_a = valor_b 
    valor_b = temp
    return valor_a, valor_b

entero_d = 5
entero_e = 10
entero_f, entero_g = por_valor(entero_d, entero_e)

print(f"{entero_d}, {entero_e}")
print(f"{entero_f}, {entero_g}")

# Por referencia

def por_referencia(valor_a: list, valor_b: list) -> tuple:
    temp = valor_a
    valor_a = valor_b
    valor_b = temp
    return valor_a, valor_b

    lista_e [5, 10]
    lista_b [50, 100]
    lista_g, lista_h = por_referencia(lista_e, lista_f)

    print(f"{lista_e}, {lista_f}")
    print(f"{lista_g}, {lista_h}")