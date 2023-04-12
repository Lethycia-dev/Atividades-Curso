
def calcularPagamento(qtdHoras, valorHora):
    horas = float(qtdHoras)
    taxa = float(valorHora)
    if horas <= 40:
        salario = horas * taxa
    else:
        horasExcd = horas - 40
        salario = 40 * taxa + (horasExcd*(1.5 * taxa))        
    return salario

strHoras = input("Digite as horas: ")
strTaxa = input("Digite a taxa: ")
totalSalario = calcularPagamento(strHoras, strTaxa)
print("O valor dos seus rendimentos é: ", totalSalario)

'''
#print(f"Salario:",calcularPagamento(48, 15))

def calculo(horasQtd, horaValor):
    hora = float(horasQtd)       
    taxas = float(horaValor)
    if hora <= 40:
        salario = hora * taxas
    else:
        exdHoras = hora - 40
        salario = 40 * taxas + (exdHoras * (1.5 * taxas))
    return salario
 
print(f"O valor dos seus rendimentos é: {calculo(42, 25)}")              
'''
