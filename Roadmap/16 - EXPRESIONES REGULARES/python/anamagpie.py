import re #regular expresion

'''
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
'''

# r"[0-9]+" detecta todos los caracteres numéricos 1..* | \d equivalente-dígitos | \D opuesto

text = "El día 01/10/2025 fue el día nº 1 del mes de #Octubre."

def find_num(text:str) -> list:
    return(re.findall(r"\d", text))

print(find_num("El día 01/10/2025 fue el día nº 1 del mes de #Octubre."))

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
'''

def validar_email(email: str) -> bool:
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[\w]+\.[a-zA-Z]{2,}$', email)) # estandar Regex mail Python

print(validar_email("anaua234@gmail.com")) # -> True
print(validar_email("m4il@inválido@1.2"))  # -> False

def validar_tlf(tlf: str) -> bool:
    return bool(re.match(r'^\+?[\d\s]{3,}$', tlf)) # mínimo 3 dígitos | \s espacios | \+?

print(validar_tlf("+34 985434355")) # -> True
print(validar_tlf("-4 9+ç55"))      # -> False

def validar_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]+$", url)) #[s]? -> la s es opcional

print(validar_url("https://ana.ana"))    # completa -> True
print(validar_url("http://ana.ana"))     # sin s en https -> True
print(validar_url("http://www.ana.ana")) # (www.)? -> True
print(validar_url("http://w.ana.ana"))   # w -> False
print(validar_url("tp://w.ana.ana"))     # tp:// - > False