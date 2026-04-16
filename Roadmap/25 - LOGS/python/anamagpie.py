import logging
import time

'''
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
'''

#Configuración 

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')
    
#Ejemplos se menor a mayor nivel

logging.debug("Ejemplo de DEBUG: Información detallada. Usualmente para diagnosticar problemas.")
logging.info("Ejemplo de INFO: Confirmación de que el programa funciona correctamente.")
logging.warning("Ejemplo de WARNING: Advertencia de algo presente o futuro. Ej. Poco espacio en disco.")
logging.error("Ejemplo de ERROR: El software no ha podido realizar alguna función.")
logging.critical("Ejemplo de CRITICAL: El programa no puede seguir corriendo.")

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la 
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 
'''
print("---------------------------------------------------------------")

class Tareas:

    def __init__(self) -> None:
        self.tareas = {}

    def añadir_t(self, nom: str, desc: str):
        start = time.time()
        if nom not in self.tareas:
            self.tareas[nom] = desc
            logging.info(f"Nueva tarea añadida: {nom}.")
        else:
            logging.warning(f"La tarea '{nom}' ya existe.")
            logging.debug(f"Número de tareas: {len(self.tareas)}")
            end = hora.time()
            self.hora(start, end)

    def borrar_t(self, nom: str):
        start = time.time()
        if nom in self.tareas:
            del self.tareas[nom]
            logging.info(f"La tarea '{nom}' ha sido eliminada.")
        else:
            logging.error(f"No es posible eliminar porque la tarea '{nom} ya existe.")
            logging.debug(f"Número de tareas: {len(self.tareas)}")
            end = time.time()
            self.hora(start, end)

    def listar_t(self):
        start = time.time()
        if self.tareas:
            logging.info("Lista de tareas: ")
            for nom, desc in self.tareas.items():
                print(f"{nom} - {desc}")
        else:
            logging.info("La lista de tareas está vacía.")
            end = hora.time()
            self.hora(start, end)


    def hora(self, start, end): 
        logging.debug(f"Tiempo de ejecución de la tarea {nom}: {end - start:.6f} sec.")
        #.6f = . = decimal | 6 = 6 decimales | fixed = muestra decimales aunque sean ceros

task_m = Tareas()

task_m.añadir_t("Badat", "Estudiar Bases de Datos.")
task_m.añadir_t("Perro", "Sacar al perro.")
task_m.añadir_t("Comida", "Reservar mesa para cinco personas.")
task_m.borrar_t("Badat")
task_m.listar_t()
task_m.añadir_t("Compra", "Comprar regalo para Paula.")
task_m.listar_t()
