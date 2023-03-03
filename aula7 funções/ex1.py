def calcularPagamento(qtdHoras, valorHora):
    horas = float(qtdHoras)
    taxa = float(valorHora)
    if horas <= 40:
        salario = horas * taxa
    else:
        horasExcd = horas - 40
        salario = 40 * taxa + (horasExcd*(1.5 * taxa))        
    return salario
'''
strHoras = input("Digite as horas: ")
strTaxa = input("Digite a taxa: ")
totalSalario = calcularPagamento(strHoras, strTaxa)
print("O valor dos seus rendimentoe é: ", totalSalario)
'''

print(f"Salario:",calcularPagamento(48, 15))
       