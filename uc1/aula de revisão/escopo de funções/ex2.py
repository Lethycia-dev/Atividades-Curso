#Escreva um programa que solicite ao usuário um número e imprima se esse número é par ou ímpar. Crie uma função para determinar se um número é par e outra função para determinar se um número é ímpar.


def main():
    global num
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        par()
    else:
        impar()    

def par():
    print(f"{num} é um numero par")

def impar():
    print(f"{num} é um numero impar")

main()    