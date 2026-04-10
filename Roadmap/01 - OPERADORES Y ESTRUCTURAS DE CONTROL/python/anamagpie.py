#OPERADORES Y ESTRUCTURAS DE CONTROL

#Operandores asitméticos
print(f"Suma: 10 + 5 = {10 + 5}") #entre llaves si opera
print(f"Resta: 10 - 5 = {10 + 5}")
print(f"Multiplicación: 10 * 5 = {10 + 5}")
print(f"División: 10 / 5 = {10 / 5}")
print(f"Módulo: 10 % 5 = {10 % 5}")
print(f"Eponente: 10 ** 5 = {10 ** 5}")
print(f"División Entera: 10 // 5 = {10 // 5}")

#Operadores de comparación
print(f"Igualdad: 10 == 5 es {10 == 5}") #false 
print(f"Desigualdad: 10 != 5 es {10 != 5}") #true 
print(f"Mayor que: 10 > 5 es {10 > 5}")
print(f"Menor que: 10 < 5 es {10 < 5}")
print(f"Mayor o igual que: 10 >= 5 es {10 >= 5}")
print(f"Menor o igual que: 10 <= 5 es {10 <= 5}")

#Operadores lógicos
print(f"AND &&: 10 + 5 == 15 and 5 - 1 == 4 es {10 + 5 == 15 and 5 - 1 == 4}") #todos tienen que ser verdaderos
print(f"OR ||: 10 + 5 == 15 or 5 - 1 == 4 es {10 + 5 == 15 or 5 - 1 == 4}") #al menos uno debe de ser verdadero
print(f"NOT !: not 10 + 5 == 1 {not 10 + 5 == 1}")

#Operadores de asignación
num = 15 #asignación
print(num)

num += 5 #suma y asignación
print(num)
num -= 5 #resta y asignación
print(num)
num *= 5 #multiplica y asignación
print(num)
num /= 5 #divide y asignación
print(num)

num %= 5 #Módulo y asignación
print(num)
num **= 1 #Exponente y asignación
print(num)
num //= 1 #División entera y asignación
print(num)

#Operadores de identidad
print(f"'a' in 'ana' = {'a' in 'ana'}") #true
print(f"'h' in 'ana' = {'h' in 'ana'}") #false
print(f"'h' not in 'ana' = {'h' not in 'ana'}") #true

#Operadores de bit
a = 10
b = 3
print(f"AND: 10 & 3 = {10 & 3}") 
print(f"OR: 10 | 3 = {10 | 3}")
print(f"XOR: 10 ^ 3 = {10 ^ 3}")
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") #010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") #101000

'''
Estructuras de control
'''''

#Condicionales

cadena = "ana"

if cadena == "ana":
    print("cadena es 'ana'")
elif cadena == "Cadena":
    print("cadena es 'urraca'")
else:
    print("cadena no es 'ana' ni 'urraca'")

# Iterativas

for i in range(11): #imprime del 1 al 10
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1 #imporante para que pare la cuenta

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

'''
Extra: 
Numeros comprendidos entre el 10 al 55 (incluidos) pares.
Que no aparezca el 16. 
Que no sean múltiplos de 3.
'''

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
