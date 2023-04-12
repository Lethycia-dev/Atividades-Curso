class Funcionario:

    def __init__(self, nome, salario, faltas):

        self.nome = nome
        self.salario = salario
        self.faltas = faltas

    def aumentarSalario(self,valorAumento):
        
        self.salario = self.salario + valorAumento

    def descontarFalta(self):
        
        valorfaltas = (self.salario / 30) * self.faltas
        self.novosalario = self.salario - valorfaltas
        

    def informacoes(self):
        
        informacao = f'¬ Nome - {self.nome}, Salário - R${self.salario} e Faltas - {self.faltas}.'
        return informacao
    
    def informacaoAtualizada(self):
        
        informacaoAtual = f'¬ Nome - {self.nome}, Salário - R${self.novosalario:.2f} e Faltas - {self.faltas}.'
        return informacaoAtual

funcionario1 = Funcionario('Jhosephe', 7700, 7)

print(funcionario1.informacoes())

funcionario1.aumentarSalario(2000)

funcionario1.descontarFalta()

print(funcionario1.informacaoAtualizada())


