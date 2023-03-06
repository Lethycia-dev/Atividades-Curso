'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

'''

def questao1():
    n = int(input("Digite um numero: "))
    nFinal = n
    for i in range(nFinal != 100):
        if n == 100:
            print(nFinal)
        elif n > 0:
            print(n)
            nFinal = n + 1
            print(nFinal)    
    

print(questao1())
