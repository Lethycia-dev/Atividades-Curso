'''
2. Classe Funcionário: Implemente a classe Funcionário. Um funcionário tem um
nome e um salário. Escreva um construtor com dois parâmetros (nome e salário) e
o método aumentarSalario (porcentualDeAumento) que aumente o salário do
funcionário em uma certa porcentagem. Exemplo de uso: harry = f u n c i o n á r i o
( " H a r r y " , 2 5 0 0 0 ) harry.aumentarSalario(10) Faca um programa que teste o
método da classe.
'''

class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def aumentarSalario(self,percentualDeAumento):
        self.salario = self.salario * (100 + percentualDeAumento)/100
        return self.salario
    
harry = Funcionario("Harry", 25000)
harry.aumentarSalario(10)

print("aumento de : ", self.salario)