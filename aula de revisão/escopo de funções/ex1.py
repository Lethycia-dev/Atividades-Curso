#Escreva um programa que solicite ao usuário dois números e imprima a soma, a subtração, a multiplicação e a divisão desses números. Crie funções separadas para cada operação matemática.

def main():
    global num1 
    global num2 
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite um numero: "))

    soma()
    subtracao()
    multiplicacao()
    divisao()

def soma():
    print(f"{num1} + {num2} = {num1 + num2}")    

def subtracao():
    print(f"{num1} - {num2} = {num1 - num2}")

def multiplicacao():
    print(f"{num1} * {num2} = {num1 * num2}")

def divisao():
    print(f"{num1} / {num2} = {num1 / num2:,.2f}")

main()