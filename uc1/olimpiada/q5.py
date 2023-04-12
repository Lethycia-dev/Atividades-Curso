# Receba um numero inteiro e, a a partir de funções, imprima a tubuada desse numero de acordo com  vontade do operador
# O operador poderá escolher a tubuada da soma, subtração, divisão, multiplicação ou todas
# Inclua um metodo para que não seja quebrado o programado e adicione uma opção de saída para o operador
# OBS: Cuidado com a tabuada da divisão, adicione somente duas casas decimais
import random

def main():
    import random
    global num
    global operador
    global novoOperador
    operador = ['*', '/', '-', '+', '* e / e + e -']
    novoOperador = random.choice(operador)
    print(f"Seu operador é: {novoOperador}")
    
    num = int(input("Digite um numero inteiro: "))
    
    
    if novoOperador == '*':
          multiplicacao()
    elif novoOperador == '/':
          divisao()
    elif novoOperador == '-':
          subtracao()
    elif novoOperador == '+':
          adicao()
    elif novoOperador == '* e / e + e -':
         todas()      
    else:
          print("Erro")

def multiplicacao():
    print("Multiplicação: ")
    for i in range(11):
        
        print(f"{num} * {i} = {num * i}")
'''        
    print(f"{num} * 1",num * 1)
    print(f"{num} * 2",num * 2)
    print(f"{num} * 3",num * 3)
    print(f"{num} * 4",num * 4)
    print(f"{num} * 5",num * 5)
    print(f"{num} * 6",num * 6)
    print(f"{num} * 7",num * 7)
    print(f"{num} * 8",num * 8)
    print(f"{num} * 9",num * 9)
    print(f"{num} * 10",num * 10)
'''
def divisao():
      print("Divisão: ")
      
      for i in range(1,11):
        
        print(f"{num} / {i} = {num / i}")
'''        
print(f"{num} * 1 = {(num / 1):.2f}")
print(f"{num} * 2 = {(num / 2):.2f}")
print(f"{num} * 3 = {(num / 3):.2f}")
print(f"{num} * 4 = {(num / 4):.2f}")
print(f"{num} * 5 = {(num / 5):.2f}")
print(f"{num} * 6 = {(num / 6):.2f}")
print(f"{num} * 7 = {(num / 7):.2f}")
print(f"{num} * 8 = {(num / 8):.2f}")
print(f"{num} * 9 = {(num / 9):.2f}")
print(f"{num} * 10 = {(num / 10):.2f}")
'''

def subtracao():
    print("Subtração: ")
    for i in range(11):
        
        print(f"{num} - {i} = {num - i}")
'''        
    print(num - 1)
    print(num - 2)
    print(num - 3)
    print(num - 4)
    print(num - 5)
    print(num - 6)
    print(num - 7)
    print(num - 8)
    print(num - 9)
    print(num - 10)
'''
def adicao():
    print("Adição: ")
    for i in range(11):
        
        print(f"{num} + {i} = {num + i}")
'''        
    print(num + 1)
    print(num + 2)
    print(num + 3)
    print(num + 4)
    print(num + 5)
    print(num + 6)
    print(num + 7)
    print(num + 8)
    print(num + 9)
    print(num + 10)
'''
def todas():
        adicao()
        subtracao()
        divisao()
        multiplicacao()

main()
     