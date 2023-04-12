
class Pokemon:
    def __init__(self,nome,tipo,ataque,defesa,hp,movimento):
        self._tipo = tipo
        self._nome = nome
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp
        self._movimento = movimento
    
    def batalha(self):
        pokemonEscolhido = self._ataque + self._defesa 
        pokemon2 = self._ataque + self._defesa 
        if pokemonEscolhido > pokemon2 :
            print(f"{self._nome} foi o ganhador com o {self._movimento} e ataque de {self._ataque}")
        elif pokemon2 > pokemonEscolhido:
            print(f"{self._nome} foi o ganhador com o {self._movimento} e ataque de {self._ataque}")


class Treinador:
    
  
    def __init__(self,apelido):
        self._apelido = apelido
    

class Jogador(Treinador):
    def __init__(self, listaPokemons,pokemonEscolhido):
        super().__init__(listaPokemons,pokemonEscolhido)
        self.pokemonEscolhido = pokemonEscolhido
        print()
        play = input("digite o numero do pokemon escolhido: ")
        if play == 1:
            pokemonEscolhido = Pokemon("pikachu","eletrico","500","500","1200","choque do trovão")   
        elif play == 2:
            pokemonEscolhido = Pokemon("pikachu","eletrico","500","500","1200","choque do trovão")
        elif play == 3 :
            pokemonEscolhido = Pokemon("pikachu","eletrico","500","500","1200","choque do trovão")
        elif play == 4:
            pokemonEscolhido = Pokemon("pikachu","eletrico","500","500","1200","choque do trovão")    
        else:
            print("numero invalido")
        


class Inimigo(Treinador):
    def __init__(self, listaPokemons):
        super().__init__(listaPokemons)        


p1 = Treinador("mayra")
print(p1._apelido())



