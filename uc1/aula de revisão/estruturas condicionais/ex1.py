#Escreva um programa que solicite ao usuário um número e imprima se ele é positivo, negativo ou zero.

num = int(input("Digite um numero: "))
if num == 0:
    print(f"{num} é igual a 0")
elif num > 0:
    print(f"{num} é positivo")
elif num < 0:
    print(f"{num} é negativo")        
else:
    print("Numero invalido")    

#Programa solicita um numero ao usuario e armazena essa informação em uma variavel chamada {num}
# em seguida inicia um estrutura condicional no qual:
# se o numero digitado for 0 o programa exibira que o {num} é zero
# senao se o numero digitado for maior que 0 o programa imprimira que ele é positivo
# senao se o numero digitado for menor que 0 o programa exibira que ele é negativo 
# se nao o programa exiira que o numero digitado esta invalido    