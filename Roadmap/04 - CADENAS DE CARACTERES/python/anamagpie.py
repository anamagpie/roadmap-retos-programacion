'''
CADENAS DE CARACTERES
'''

# Operaciones

s1 = "Hola"
s2 = "Python"

#Concatenación
print(s1 + s2)
print(s1 + " " + s2 + ".")

#Repetición
print(s1 * 3)

#Indexaciónext
print(s1[0] + s1[3] + s1[0] + s1[3] + s1[0] + s1[3] + "!!!!!")

#Longitud
print(len(s2))

#Slicing (porción) // El índice final no se tiene en cuenta
print(s2[2:6])
print(s2[:6]) 
print(s2[2:])

#Búsqueda
print("a" in s1)
print("i" in s1)

#Reemplazo
print(s1.replace("o", "a"))

#División
print(s2.split("t"))  #Corta y desaparece la T

#Mayus Minus
print(s1.upper())
print(s1.lower())
print("probando cosas con mayus y minus".title())
print("probando más cosas con mayus y minus".capitalize())

#Eliminación de espacios al principio y al final
print(" cosas con espacios ".strip())

#Búsqueda al principio y al final
print(s1.startswith("Ho"))

#Búsqueda por posición
print("Voy a buscar cosas según su posición".find("cosas")) 

#También puedo hacerlo así
s3 = "Creo que también puedo hacerlo así"

print(s3.find("t"))
print(s3.find("puedo"))

# Formateo
print("Saludo: {} , lenguaje: {}!".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguaje: {s2}!")

#Transformación en lista de caracteres
print(list(s3))

l1 = [s1, ", ", s2, "!"]
print("".join(l1))

#TRansformaciones numéricas
s4 = "123456"
s4 = int(s4) #transforma en numero entero
print(s4)

#Comprobaciones varias
print(s1.isalnum())
print(s1.isalpha())

'''
Extra
'''

def check(word1: str, word2: str):

    #Palíndromo
    print(f"Dime si {word1} es un palíndromo: {word1 == word1[::-1]}")
    print(f"Dime si {word2} es un palíndromo: {word2 == word2[::-1]}")

    #Anagramas
    print(f"Dime si {word1} es un anagrama de {word2}: {sorted(word1) == sorted(word2)}")

    #Isograma
    print(f"Dime si {word1} es un isograma: {len(word1) == len(set(word1))}")
    print(f"Dime si {word1} es un isograma: {len(word2) == len(set(word2))}")

    word_dict = dict()
    for word in word1:
        word_dict[word] = word_dict.get(word, 0) + 1

    for word in word_dict:
        print(word_dict)
    
check("radar", "python")
check("amor", "roma")
