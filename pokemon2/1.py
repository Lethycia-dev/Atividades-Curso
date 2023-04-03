import pokedex
import random

class Pokemon:
    def __init__(self,nome,tipo,ataque,defesa,hp):
        self._nome = nome
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp
   
class Agua(Pokemon):
    def __init__(self, nome, tipo, ataque, defesa, hp):
        super().__init__(nome, tipo, ataque, defesa, hp)

class Fogo(Pokemon):
    def __init__(self, nome, tipo, ataque, defesa, hp):
        super().__init__(nome, tipo, ataque, defesa, hp)

class Grama(Pokemon):
    def __init__(self, nome, tipo, ataque, defesa, hp):
        super().__init__(nome, tipo, ataque, defesa, hp)

class Treinador:
    def __init__(self,nome,listaPokemons):
      
        self._nome = nome
        self._listaPokemons = listaPokemons
        listaPokemons = []
        

        def escolherPokemon(self):
            print(random.choice(self.pokedex))
            return escolherPokemon
        
    def capturarPokemon(self,novoPokemon):
       self._novoPokemon = novoPokemon
       novoPokemon = random[pokedex]

    def listarPokemons(self): 
        print("Sua lista de pokemons: ")
        for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")
   

def batalha(play1,play2):
  
    p1 = play1
    p2 = play2

    p1Forca = (p1._ataque + p1._defesa + p1._hp) 
    p2Forca = (p2._ataque + p2._defesa + p2._hp) 

    print(f"{p1._nome} atacou com {p1._movimento} e força {p1Forca}")
    print(f"{p2._nome} atacou com {p2._movimento} e força {p2Forca}")

    if (p1Forca > p2Forca):
        print(f"O vencedor foi {p1._nome} com força {p1Forca} do treinador {play1._nome}")
    elif (p1Forca < p2Forca):
        print(f"O vencedor foi {p2._nome} com força {p2Forca} do treinador {play2._nome}")
    else:
        print("Deu empate")
        

class Jogador(Treinador):
    def __init__(self, nome, listaPokemons):
        super().__init__(nome, listaPokemons)  



    def escolherPokemon(self): 
        while True:
            print(f"Escolha seu pokemon: ")

            self._listaPokemons()

            pokemonEscolhido = input("Digite o número do pokemon escolhido: ")

           
            if (pokemonEscolhido.isnumeric()):
                if (int(pokemonEscolhido) <= len(self._pokemons)):
                    return self._pokemons[int(pokemonEscolhido)-1]
                else:
                    print("Você escreveu um número maior do que o disponível.")
            else: 
                print("Você escreveu um caractere inválido")      
           

class Inimigo(Treinador):
    def __init__(self, nome, listaPokemons):
        super().__init__(nome, listaPokemons)
        

print(f'''

Primeiro pokemon:

{random.choice[pokedex]}


''')


while True:

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
            batalha()
        case "3":
            print("saindo...")
            break     
