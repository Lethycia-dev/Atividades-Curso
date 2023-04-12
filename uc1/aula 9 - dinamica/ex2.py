'''
Q.2 Elabore um algoritmo que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 reais.

'''


def saque():

    nota1 = 0
    nota2 = 0
    nota5 = 0
    nota10 = 0
    nota20 = 0
    nota50 = 0
    nota100 = 0


    contador = 0
    valorSaque = input("Digite o valor do saque: ")
    lista = ['']
    lista.append(valorSaque)
    for i in len(lista[::-1]):
        if i == '1':
            if i in len(lista) == '2':
                pass
            else:    
                nota1 += 1
        if i == '2':
            contador += 1