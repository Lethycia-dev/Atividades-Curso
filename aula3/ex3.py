numeros = 0 
menor = 0

for i in range(5):
    numeros = int(input("Digite um numero inteiro: "))

    if menor == 0:
        menor = numeros

    elif numeros < menor:
        menor = numeros


print(f" O menor valor é : {menor}")