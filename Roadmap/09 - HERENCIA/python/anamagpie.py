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
        print("Perro: Sácame a la calle!!!")

class Gato(Animal): #Subclase Gato

    def sonido(self):
        print("Gato: Dame una latita!!!")

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
print("_____________________________________") #Separador

class Empleado:

    def __init__(self, iden: int, nombre: str):
        self.nombre = nombre
        self.iden = iden
        self.empleados = []

    def add(self, empleado):
       self.empleados.append(empleado)
    
    def print_empleados(self):
        for empleado in self.empleados:
            print(empleado.nombre)


class Gerente(Empleado):

    def coordinar_empresa(self):
        print(f"{self.nombre} asigna los proyectos a los Gerentes de Proyectos.")


class GerenteProyectos(Empleado):

    def __init__(self, iden: int, nombre: str, proyecto: str):
        super().__init__(iden, nombre)
        self.proyecto = proyecto

    def coordinar_proyectos(self):
        print(f"{self.nombre} coordina los proyectos de la empresa y dirige al grupo de programadores.")


class Programador(Empleado):

    def __init__(self, iden: int, nombre: str, proyecto: str, lenguaje: str):
        super().__init__(iden, nombre)
        self.proyecto = proyecto
        self.lenguaje = lenguaje
    
    def programar(self):
        print(f"{self.nombre} trabaja dentro del {self.proyecto} en leguaje {self.lenguaje}")

    def add(self, empleado: Empleado):
        print(f"Los programadores no tienen empleados a su cargo. {empleado.nombre} no se añadirá.")


new_gerente = Gerente(121314, "Inés Ramiro González")
new_gerente_pro1 = GerenteProyectos(222324, "Dolores Álvarez Silva", "Proyecto Sostenibilidad")
new_gerente_pro2 = GerenteProyectos(222325, "Joaquín León López", "Proyecto Digitalización")
new_programador1 = Programador(323334, "Luis Ramiro Gómez", "Proyecto Sostenibilidad", "Java")
new_programador2 = Programador(323335, "Jose María Riberio Suárez", "Proyecto Digitalización", "Java")
new_programador3 = Programador(323336, "Alba Domingo González", "Proyecto Sostenibilidad", "Python")
new_programador4 = Programador(323337, "Laura Francisco Jimenez", "Proyecto Digitalización", "Python")

new_gerente.add(new_gerente_pro1)
new_gerente.add(new_gerente_pro2)

new_gerente_pro1.add(new_programador1)
new_gerente_pro1.add(new_programador2)
new_gerente_pro2.add(new_programador3)
new_gerente_pro2.add(new_programador4)

new_programador1.add(new_programador2)

new_programador1.programar()
new_gerente_pro1.coordinar_proyectos()
new_gerente.coordinar_empresa()

new_gerente.print_empleados()
new_gerente_pro1.print_empleados()
new_programador1.print_empleados()







    

'''
    def iden(self):
        print("El id de Programadores es 444546-C")

    def nombre(self):
        print("Nombre del Gerente de Proyectos es: Inés Martín Suárez")  


def print_identificador(empleados: Empleados):
    empleados.identificador()
def print_nombre(empleados: Empleados):
    empleados.nombre() 

new_empleados = Empleados("Empleados")
print_identificador(new_empleados)
new_gerentes = Gerentes("Gerentes")
print_identificador(new_gerentes)
new_gerentes_pro = GerentesDeProyectos("Gerentes de Proyectos")
print_identificador(new_gerentes_pro)
new_programadores = Programadores("Programadores")
print_identificador(new_programadores)
'''
    