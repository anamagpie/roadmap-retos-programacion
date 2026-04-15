import requests
 
'''
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
'''
'''
respuesta = requests.get("https://google.com")
if respuesta.status_code == 200:
    print(respuesta.text)
else:
    print(f"Error {respuesta.status_code}.")
'''
'''
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
'''

print("___________________________________________________________________________")

print("¡Hola, Entrenador! Aquí tienes toda la info sobre tus Pokémon.")
nombre = input("Para empezar, ¿cómo te llamas?: ")
print("¡Bienvenido " + nombre + "!")
pokemon = input("Introduce el nombre del Pokémon que quieres buscar: ").lower()

respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")

if respuesta.status_code == 200:
    data = respuesta.json()

    print("Nombre: ", data["name"])
    print("---------------------------")
    print("ID: ", data["id"])
    print("---------------------------")
    print("Peso: ", data["weight"])
    print("---------------------------")
    print("Altura: ", data["height"])
    print("---------------------------")
    print("Tipo/s: ")
    for type in data["types"]:
        print(type["type"]["name"])
    print("---------------------------")
    print("Juegos: ")
    for game in data["game_indices"]:
        print(game["version"]["name"])
    print("---------------------------")

    respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")

    if respuesta.status_code == 200:
        url = respuesta.json()["evolution_chain"]["url"]
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            data = respuesta.json()
            print(f"Evoluciones de {pokemon}: ")
            print("---------------------------")

            def evoluciones(data):
                print(data["species"]["name"])
                if "evolves_to" in data:
                    for evolve in data["evolves_to"]:
                        evoluciones(evolve)
            
            evoluciones(data["chain"])

        else:
            print(f"Error {respuesta.status_code} al intentar obtener las evoluciones de {pokemon}.")

    else:
        print(f"Error {respuesta.status_code} al intentar obtener las evoluciones de {pokemon}.")
    
else:
    print(f"Error {respuesta.status_code}. No tenemos a ese Pokémon registrado.")