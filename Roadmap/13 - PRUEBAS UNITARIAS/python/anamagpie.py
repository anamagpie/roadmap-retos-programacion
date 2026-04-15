import unittest
from datetime import datetime, date

'''
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.

'''

def sum(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales.")
    return num1 + num2


class TestSum(unittest.TestCase):

    def test_sum(self): #
        self.assertEqual(sum(5, 7), 12) # 12 es el valor esperado de la suma 5 + 7
        self.assertEqual(sum(10, -7), 3)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(3.5, 5.1), 8.6)
        self.assertEqual(sum(2, 2.6), 4.6)
        self.assertEqual(sum(2.5, 12), 14.5)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(10, "-7")
        with self.assertRaises(ValueError):
            sum("y", 6)
        with self.assertRaises(ValueError):
            sum(None, 12)

'''

 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.

'''


class TestData(unittest.TestCase):

    def setUp(self) -> None:
        self.data = {
            "nombre": "Ana",
            "num_alumn": 46,
            "fecha_ing": datetime.strptime("01-10-25", "%d-%m-%y").date(),
            "leng_prog": ["Python", "Java", "Javascript", "SQL"]
        }

    def test_fields_exist(self):
        self.assertIn("nombre", self.data)
        self.assertIn("num_alumn", self.data)
        self.assertIn("fecha_ing", self.data)
        self.assertIn("leng_prog", self.data)

    def test_data_is_correct(self):
        self.assertIsInstance(self.data["nombre"], str)
        self.assertIsInstance(self.data["num_alumn"], int)
        self.assertIsInstance(self.data["fecha_ing"], date)
        self.assertIsInstance(self.data["leng_prog"], list)


unittest.main()