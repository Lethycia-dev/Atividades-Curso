class Pokemon:
    def __init__(self,ataque,defesa,nome,tipo,hp,movimento):
        self._ataque = ataque 
        self._defesa = defesa 
        self._especie = nome
        self._tipo = tipo
        self._hp = hp
        self._movimento = movimento

    def fazerBarulho(self):
        print(f"{self.nome} fez alguma coisa ")  

    def ataque(self):
        print(f"O {self._nome} atacou com {self._movimento}")
    
    def batalha(self,oponente):
        if play1(self._ataque) + (self._defesa) >  play2(self._ataque) + play2(self._defesa):
            pokemonWin = play1(self._nome)
            print(f"ganhador é {pokemonWin}")           


class PokemonFogo(Pokemon):
    def __init__(self, especie, tipo, hp, movimento):
        super().__init__(especie, tipo, hp, movimento)        

class PokemonAgua(Pokemon):
    def __init__(self, especie, tipo, hp, movimento):
        super().__init__(especie, tipo, hp, movimento)

class PokemonGrama(Pokemon):
    def __init__(self, especie, tipo, hp, movimento):
        super().__init__(especie, tipo, hp, movimento)                

play1 = Pokemon("500","400","caca","grama","1200","doido","papa")        
play2 = Pokemon("100","300","dada","grama","1000","doido","rara")        

