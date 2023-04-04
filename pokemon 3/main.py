import random 
import pokedex

class Pokemon:  
    def __init__(self, nome, tipo, ataque, defesa):
        self._nome = nome 
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
      

class Agua(Pokemon):
    def __init__(self, nome, tipo, ataque, defesa ):
        super().__init__(nome, tipo, ataque, defesa )
        self._tipo = "Água"
      
class Fogo(Pokemon):
    def __init__(self, nome, tipo, ataque, defesa ):
        super().__init__(nome, tipo, ataque, defesa )
        self._tipo = "Fogo"
      
class Grama(Pokemon):
    def __init__(self, nome, tipo, ataque, defesa ):
        super().__init__(nome, tipo, ataque, defesa )
        self._tipo = "Grama"
class Inseto(Pokemon):
    def __init__(self, nome, tipo, ataque, defesa):
        super().__init__(nome, tipo, ataque, defesa)
        self._tipo = "Inseto"

class Venenoso(Pokemon):
    def __init__(self, nome, tipo, ataque, defesa):
        super().__init__(nome, tipo, ataque, defesa)
        self._tipo = "Venenoso"

class Normal(Pokemon):
    def __init__(self, nome, tipo, ataque, defesa):
        super().__init__(nome, tipo, ataque, defesa)
        self._tipo = "Normal"                

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
      
        print(self._listaPokemons)
        

    def capturarPokemon(self):

        listaAleatoria = []
        

        while len(listaAleatoria) < 3:
           
            pokemonAleatorio = random.choice(pokedex.pokemons)
            match pokemonAleatorio['tipo']:
                case 'Água':
                    novoPokemon = Agua(pokemonAleatorio['nome'],pokemonAleatorio['tipo'],pokemonAleatorio['ataque'],pokemonAleatorio['defesa'])
                    
                case 'Fogo':
                    novoPokemon = Fogo(pokemonAleatorio['nome'],pokemonAleatorio['tipo'],pokemonAleatorio['ataque'],pokemonAleatorio['defesa'])

                case 'Grama': 
                    novoPokemon = Grama(pokemonAleatorio['nome'],pokemonAleatorio['tipo'],pokemonAleatorio['ataque'],pokemonAleatorio['defesa'])

                case 'Inseto':
                    novoPokemon = Inseto(pokemonAleatorio['nome'],pokemonAleatorio['tipo'],pokemonAleatorio['ataque'],pokemonAleatorio['defesa'])
                case 'Venenoso':
                    novoPokemon = Venenoso(pokemonAleatorio['nome'],pokemonAleatorio['tipo'],pokemonAleatorio['ataque'],pokemonAleatorio['defesa'])
                case 'Normal':
                    novoPokemon = Normal(pokemonAleatorio['nome'],pokemonAleatorio['tipo'],pokemonAleatorio['ataque'],pokemonAleatorio['defesa'])
    

            listaAleatoria.append(novoPokemon)

        contador = 1
        for pokemon in listaAleatoria:
            print(f"{contador} - {pokemon._nome}")
            contador += 1 

        op = int(input("Digite o pokemon que você deseja:"))
        match op:
            case "1":
                self._listaPokemons.append(op-1)

            case "2":    
                self._listaPokemons.append(op-1)
            case "3":
                self._listaPokemons.append(op-1)

              
               
                    
           
                
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
            Jogador.capturarPokemon("pokemon")

        case "2":
            Jogador.escolherPokemon("pokemon")
            batalhaPokemon("p1","p2")
        case "3":
            print("saindo...")
            break  