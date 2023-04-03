import random 
import pokedex

class Pokemon:  
    def __init__(self, nome, tipo, ataque, defesa, hp):
        self._nome = nome 
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp
      

class Agua(Pokemon):
    def __init__(self, nome, tipo, ataque, defesa, hp):
        super().__init__(nome, tipo, ataque, defesa, hp)
        self._tipo = "agua"
      
class Fogo(Pokemon):
    def __init__(self, nome, tipo, ataque, defesa, hp):
        super().__init__(nome, tipo, ataque, defesa, hp)
        self._tipo = "fogo"
      
class Terra(Pokemon):
    def __init__(self, nome, tipo, ataque, defesa, hp):
        super().__init__(nome, tipo, ataque, defesa, hp)
        self._tipo = "terra"
      
class Treinador: 
    def __init__(self, nome, listaPokemons):
        self._nome = nome
        self._listaPokemons = listaPokemons

    def escolherPokemon(self):
        return random.choice(self._listaPokemons)

class Jogador(Treinador):
    def __init__(self, nome, listaPokemons):
        super().__init__(nome, listaPokemons)

    def escolherPokemon(self):
        contador = 1
        for pokemon in self._listaPokemons:
            print(f"{contador} {pokemon}")
            contador += 1

    def capturarPokemon(self):

        listaAleatoria = []
        

        while len(listaAleatoria) < 3:
           
            pokemonAleatorio = random.choice(pokedex.pokemons)
            match pokemonAleatorio['tipo']:
                case 'agua':
                    novoPokemon = Agua(pokemonAleatorio["nome"],pokemonAleatorio["tipo"],pokemonAleatorio,"ataque",pokemonAleatorio["defesa"],pokemonAleatorio["hp"])
                    
                case 'fogo':
                    novoPokemon = Fogo(pokemonAleatorio["nome"],pokemonAleatorio["tipo"],pokemonAleatorio,"ataque",pokemonAleatorio["defesa"],pokemonAleatorio["hp"])

                case 'terra': 
                    novoPokemon = Terra(pokemonAleatorio["nome"],pokemonAleatorio["tipo"],pokemonAleatorio,"ataque",pokemonAleatorio["defesa"],pokemonAleatorio["hp"])

            listaAleatoria.append(novoPokemon)

        contador = 1
        for pokemon in listaAleatoria:
            print(f"{contador} - {pokemon._nome}")
            contador += 1 

        op = int(input("Digite o pokemon que você deseja:"))   
        self._listaPokemons.append = listaAleatoria[op]  
      
               
                    
           
                
class Inimigo(Treinador):
    def __init__(self, nome, listaPokemons):
        super().__init__(nome, listaPokemons)


    
def batalhaPokemon(play1, play2): 

    p1 = play1.escolherPokemon()
    p2 = play2.escolherPokemon()

    forca1 = (p1._ataque + p1._defesa) 
    forca2 = (p2._ataque + p2._defesa) 

    print(f"{p1._nome} tem força de {forca1}")
    print(f"{p2._nome} tem força de {forca2}")

    if (forca1 > forca2):
        print(f"O vencedor foi {p1._nome} com força {forca1} do treinador {play1._nome}")
    elif (forca1 < forca2):
        print(f"O vencedor foi {p2._nome} com força {forca2} do treinador {play2._nome}")
    else:
        print("Empate!!")



while True :
    print('''
    Menu:

    1- Capturar Pokemon
    2- Batalha Pokemon
    3- Sair


    ''')
    op = input("Digite a opção que deseja executar: ")
    match op:
        case "1":
            Jogador.capturarPokemon()

        case "2":
            batalhaPokemon(play1="dudu",play2="dada")
        case "3":
            print("saindo...")
            break     


