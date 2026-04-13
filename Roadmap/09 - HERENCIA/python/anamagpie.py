'''
* EJERCICIO:
* Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
* implemente una superclase Animal y un par de subclases Perro y Gato,
* junto con una función que sirva para imprimir el sonido que emite cada Animal.
'''

class Animal: #Super clase

    def __init__(self, nombre: str):
        self.nombre = nombre

    def sonido(self):
       pass
        
class Perro(Animal): #Subclase Perro

    def sonido(self):
        print("Sácame a la calle!!!")

class Gato(Animal): #Subclase Gato

    def sonido(self):
        print("Dame una latita!!!")

class Loro(Animal): #Subclase Gato

    def sonido(self):
        print("El loro solo sabe imitar... ")
        texto =  input ("Prueba a escribirle algo al loro, ¡a ver que pasa!: ")
        print(texto + "..." + " crrruuu!!")
        print("Te lo dije, solo sabe imitar...")


def print_sonido(animal: Animal):
    animal.sonido()

new_animal = Animal("Animal")
print_sonido(new_animal)
new_perro = Perro("Perro")
print_sonido(new_perro)
new_gato = Gato("Gato")
print_sonido(new_gato)
new_loro = Loro("Loro")
print_sonido(new_loro)

'''
* DIFICULTAD EXTRA (opcional):
* Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
* pueden ser Gerentes, Gerentes de Proyectos o Programadores.
* Cada empleado tiene un identificador y un nombre.
* Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
* actividad, y almacenan los empleados a su cargo.
 '''