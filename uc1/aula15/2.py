# HERANÇA

class Animal:
    def __init__(self,nome,cor):
        self._nome = nome
        self._cor = cor

    def comer(self):
        print(f"{self._nome} esta comendo.")

    def correr(self):
        print(f"{self._nome} esta correndo")

class Gato(Animal):
    def __init__(self,nome,cor) -> None:
        super().__init__(nome,cor)

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)        

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def get_correr(correr):
        return correr
    def set_correr():
        def correr():
            print("pulando")
            return correr
        

gato = Animal("xanim", "preto")      
cachorro = Animal("max", "caramelo")      
coelho = Animal("nina", "branca")

gato.comer()
cachorro.comer()
coelho.comer()

gato.correr()
cachorro.correr()
coelho.correr()