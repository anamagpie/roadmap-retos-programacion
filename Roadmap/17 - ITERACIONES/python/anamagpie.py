'''
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
'''
print("Cuenta con for:")
for i in range(0,10):
    print(i + 1)

print("Cuenta con while:")
i = 1
while i <=10:
    print(i)
    i += 1

print("Cuenta con def contar():")
def contar(i=1):
    if i <= 10:
        print(i)
        contar(i + 1)

contar()


'''
 * DIFICULTAD EXTRA:
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
'''

print("Cuenta con una lista []:")
for e in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: 
    print(e)

print("Cuenta con una lista {}:")
for e in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}: 
    print(e)

print("Cuenta con un mapa:")
for e in {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j"}:
    print(e)

print("Cuenta con un mapa .values:")
for e in {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j"}.values():
    print(e)

print("Cuenta con un mapa .values:")
for e in {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j"}.keys():
    print(e)

print("Cuenta con comprehension list:")
print(*[i for i in range(1, 11)], sep="\n")

print("Cuenta con cadena de texto:")
for cadena in "Cadena de texto":
    print(cadena)

print("Cuenta con reversed (al revés):")
for e in reversed([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(e)

print("Cuenta con sorted (ordena alfabéticamente los caracteres de la palabra 'hola'):")
for e in sorted(["h", "o", "l", "a"]):
    print(e)
