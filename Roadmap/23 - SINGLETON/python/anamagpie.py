from tkinter import S

'''
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlocon un ejemplo genérico.
'''

class Singleton:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Comparten el mismo ID
prueba1 = Singleton()
print(prueba1)
prueba2 = Singleton()
print(prueba2)

# Funciona: prueba 1 = prueba 2: True
print(prueba1 is prueba2)

'''
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
'''
#rpsr.

class UserSession:

# Instancia
    _instance = None

# Datos del usuario
    id: int = None
    username: str = None
    name: str = None
    email: str = None

#Igual que en primer ejercicio
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

# Permite asignar un usuario
    def set_user(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

# Recupera los datos del usuario
    def get_user(self):
        return f"{self.id}, {self.username}, {self.name}, {self.email}"

# Borra los datos de la sesión
    def clear_user(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None

# Asigna al usuario "inventpers0n"
session1 = UserSession()
print(session1.get_user())
session1.set_user(135455, "inventpers0n", "Invent Person", "inv_pers0n@inve.com")
print(session1.get_user())

# Recupera los datos de "inventpers0n"
session2 = UserSession()
print(session2.get_user())

# Borra los datos de la sesión
session3 = UserSession()
session3.clear_user()
print(session3.get_user())