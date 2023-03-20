class Funcionario:

    def __init__(self, nome, salario, faltas) -> None:

        self.nome = nome
        self.salario = salario
        self.faltas = faltas

    def aumentarSalario(self,valorAumento):
        
        self.novoSalario = self.salario + valorAumento

    def descontarFalta(self):
        
        valorfaltas = (self.salario / 30) * self.faltas
        self.descontarfalta = self.salario - valorfaltas
        

    def informacoes(self):
        
        informacao = f'¬ Nome - {self.nome}, Salário - {self.salario} e Faltas - {self.faltas}.'
        return informacao
    
    def informacaoAtualizada(self):
        
        informacaoAtual = f'¬ Nome - {self.nome}, Salário - {self.descontarfalta} e Faltas - {self.faltas}.'
        return informacaoAtual

funcionario1 = Funcionario('Jhosephe', 7700, 11)

print(funcionario1.informacoes())
funcionario1.descontarFalta()
funcionario1.aumentarSalario(2000)
print(funcionario1.informacaoAtualizada())


