'''
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
'''

import os
import xml.etree.ElementTree as xml
import json

data = {
    "nombre": "Ana",
    "fechanac": "02 de Febrero",
    "centro": "Universidad Laboral",
    "asignaturas": ["Bases de Datos", "Programación", "Lenguajes de Marcas", "Sistemas Informáticos"]
}

xml_file = "anamagpie.xml"
json_file = "anamagpie.json"


#XML -------------------------------------------------------------------

def create_xml():

    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file)


create_xml()

with open(xml_file, "r") as xml_data:
    print(xml_data.read())

os.remove(xml_file)

# JSON ----------------------------------------------------------------

def create_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)


create_json()

with open(json_file, "r") as json_data:
    print(json_data.read())

os.remove(json_file)


'''
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
'''

create_xml()
create_json()


class Data:

    def __init__(self, nombre, fechanac, centro, asignaturas) -> None:
        self.nombre = nombre
        self.fechanac = fechanac
        self.centro = centro
        self.asignaturas = asignaturas


with open(xml_file, "r") as xml_data:

    root = xml.fromstring(xml_data.read())
    nombre = root.find("nombre").text
    fechanac = root.find("fechanac").text
    centro = root.find("centro").text
    asignaturas = []
    for item in root.find("asignaturas"):
        asignaturas.append(item.text)

    xml_class = Data(nombre, fechanac, centro, asignaturas)
    print(xml_class.__dict__)

with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["nombre"],
        json_dict["fechanac"],
        json_dict["centro"],
        json_dict["asignaturas"]
    )
    print(json_class.__dict__)

os.remove(xml_file)
os.remove(json_file)