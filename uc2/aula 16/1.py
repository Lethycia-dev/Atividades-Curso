import requests

for i in range(151):

    resultado = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i+1}")

    pokeDict = resultado.json()


    print(pokeDict["id"])
    print(pokeDict["name"])
    print(pokeDict["height"])
    print(pokeDict["weight"])