''' 
Funciones
'''

# ------ Simple
def saludar():
    print("Hola, estás usando Python")

saludar()

# ------ Con retorno

def return_saludar():
    return "Esto es Python"
print(return_saludar())

# ------ Función con argumento 

def args_saludar(name):
    print(f"Hola, {name}")

args_saludar("Ana")
    
def args_saludar(saludar, name):
    print(f"{saludar}, {name}, estoy usando dos argumentos!!")

args_saludar("Hi", "Ana")
args_saludar(name="Ana", saludar="Hi")

# ------ Con un argumento predeterminado

def default_arg_saludar(name="Python"):
    print(f"Hola, {name} (otra vez)")

default_arg_saludar("Ana")
default_arg_saludar()

# ------ Con argumentos y retorno
def return_args_saludar(saludar, name):
    return f"{saludar}, {name}!"

print(return_args_saludar("Hi", "Ana")) #nohacecaso

# ------ Con retorno de varios valores (tupla)

def multiple_return_saludar():
    return "Hola", "Python"

saludar, name = multiple_return_saludar()
print(saludar)
print(name)

# ------ Con un número variable de argumentos

def variable_arg_saludar(*names):
    for name in names:
        print(f"Hola, {name}!!!")

variable_arg_saludar("Ana", "Python", "TSK")

# ------ Con un número variable de argumentos con palabra clave

def variable_key_arg_saludar(**names):
    for key, value in names.items():
        print(f"Hola, {value} ({key})")

        variable_key_arg_saludar(
            language="Python",
            name="Ana",
            centro="La Laboral",
            ciudad="Gijón"
        )
