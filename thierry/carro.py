class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def informacoes(self):
        print(f'{self.marca} - {self.modelo} - {self.ano}')
        
    def acelerar(self):
        velocidade = '80km/h'
        print(f'O Carro {self.marca} {self.modelo} acelerou {velocidade}.')
        
carro1 = Carro('Fiat','Uno','2000')

carro1.informacoes()
carro1.acelerar()
        