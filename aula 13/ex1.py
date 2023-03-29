class Pokemon():
    def __init__(self,nome,ataque,defesa,vida):
        self.nome = nome
        self.atk = ataque
        self.dfsa = defesa
        self._vida = vida


pokemon1 = Pokemon("Pikachu",1000,600)
pokemon2 = Pokemon(nome="charmander", ataque=800,defesa=550)

print(f"Este é o {pokemon1.nome} tem ataque de {pokemon1.atk} e defesa de {pokemon1.dfsa}")
print(f"Este é o {pokemon2.nome} tem ataque de {pokemon2.atk} e defesa de {pokemon2.dfsa}")


def batalha(pokemon01,pokemon02):

    pokemonWin = ""

    pokemon1 = pokemon01
    pokemon2 = pokemon02

    print(f"{pokemon1.nome} tem o total de {pokemon1.atk + pokemon1.dfsa} de força")
    print(f"{pokemon2.nome} tem o total de {pokemon2.atk + pokemon2.dfsa} de força")
    
    if pokemon1.atk + pokemon1.dfsa > pokemon2.atk + pokemon2.dfsa:

        pokemonWin = pokemon1.nome
        
    else:
        pokemonWin = pokemon2.nome 
    print(f"O pokemon ganhador foi o {pokemonWin}")    

batalha(pokemon1,pokemon2)