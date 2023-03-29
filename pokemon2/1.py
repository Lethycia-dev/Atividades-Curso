class Pokemon:
    def __init__(self,nome,tipo,ataque,defesa,hp):
        self._nome = nome
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp
    
    def batalha(self):
        pass

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

class Jogador(Treinador):
    def __init__(self, nome, listaPokemons):
        super().__init__(nome, listaPokemons)        

class Inimigo(Treinador):
    def __init__(self, nome, listaPokemons):
        super().__init__(nome, listaPokemons)

