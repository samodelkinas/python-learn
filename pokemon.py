import requests
import json
import datetime


def logger(func):
    def wrapper():
        with open("log.txt", "a") as logfile:
            start = datetime.datetime.now()
            try:
                result = func()
            except Exception as e:
                logfile.write(
                f"[ERR] - {datetime.datetime.now()} - {func} error {e}\n")
            finish = datetime.datetime.now()
            logfile.write(
                f"[INF] - {datetime.datetime.now()} - {func} took {finish - start}\n")
            return result
    return wrapper


@logger
def get_pokemons(base_uri="https://pokeapi.co/api/v2"):
    pokemons = []
    next_uri = None
    while True:
        uri = f"{base_uri}/pokemon" if next_uri is None else next_uri
        try:
            req = requests.get(uri)
        except requests.exceptions.ConnectionError as e:
            raise Exception("Connection error")
        except Exception as e:
            raise Exception("Unknown exception")
        if not req.status_code == 200:
            raise Exception(f"Invalid response code ({req.status_code})")
        response = json.loads(req.content)
        pokemons.extend([result['name'] for result in response['results']])
        next_uri = response['next']
        if next_uri is None:
            break
    return pokemons

@logger
def get_pokemon(id, base_uri="https://pokeapi.co/api/v2"):
    uri = f"{base_uri}/pokemon/{id}"
    response = json.loads(requests.get(uri).content)
    return {
        'weight': response['weight'],
        'abilities': ", ".join([ability['ability']['name'] for ability in response['abilities']]),
        'held items': ", ".join([held_item['item']['name'] for held_item in response['held_items']]),
    }


target_pokemon = input("Enter Pokemon name (l to list): ")
if target_pokemon == "l":
    pokemons = get_pokemons()
    for i, v in enumerate(pokemons):
        print(f"{i}\t{v}")
else:
    pokemon = get_pokemon(target_pokemon)
    for k, v in pokemon.items():
        print(f"{k}\t{v}")
