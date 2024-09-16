import requests

def formativa1(nome):
    api = "https://pokeapi.co/api/v2/"
    url = api + "pokemon/" + nome
    res = requests.get(url)
    print(res)
    if res.status_code == 200:
        pokemon = res.json()
        return pokemon
    else:
        print(f"Pokemon não encontrado! Erro: {res.status_code}")

pokemon = "pikachu"
atributos = formativa1(pokemon)

if atributos:
    print({atributos["name"]})
    print({atributos["id"]})