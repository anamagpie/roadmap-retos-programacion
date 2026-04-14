

'''
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 '''

class Persona:

    apellido: str = None 

    def __init__(self, nombre: str, edad: int, nacionalidad: str, lenguaje: list) -> None:
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.lenguaje = lenguaje

    def print(self):
        print(
            f"Nombre: {self.nombre} | Apellido: {self.apellido} | Edad: {self.edad} | Nacionalidad: {self.nacionalidad} | Lenguajes: {self.lenguaje}")

persona = Persona("David", 32, "Chile", ["Java", "Python"])
persona.print()
persona.apellido = "López"
persona.print()
persona.edad = 23
persona.print()


# Dificultad extra:

# Stack - LIFO

class Pila:

    def __init__(self):
        self.pila = []

    def push(self, item): #añadir/apilar
        self.pila.append(item)

    def pop(self): #eliminar/desapilar
        if self.count() == 0:
            return None
        return self.pila.pop()

    def count(self):
        return len(self.pila)
            
    def print(self):
        for item in reversed (self.pila):
            print(item)

new_pila = Pila()
new_pila.push("A")
new_pila.push("B")
new_pila.push("C")

print(new_pila.count())

new_pila.print()
new_pila.pop()

print(new_pila.pop())
print(new_pila.pop())
print(new_pila.pop())
print(new_pila.pop())
print(new_pila.pop())

print(new_pila.count())


# Queue - FIFO

class Cola:
    
    def __init__(self):
        self.cola = []

    def encolar(self, item):
            self.cola.append(item)

    def desencolar(self):
        if self.count() == 0:
            return None
        return self.cola.pop(0)

    def count(self):
        return len(self.cola)
            
    def print(self):
        for item in self.cola:
            print(item)


new_cola = Cola()
new_cola.encolar("A") # !!
new_cola.encolar("B")
new_cola.encolar("C")

print(new_cola.count())
new_cola.print()
new_cola.desencolar()
print(new_cola.count())
print(new_cola.desencolar())
print(new_cola.desencolar())
print(new_cola.desencolar())
print(new_cola.desencolar())
print(new_cola.desencolar())git add .
git commit -m 
