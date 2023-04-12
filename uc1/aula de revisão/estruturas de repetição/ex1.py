#Escreva um programa que imprima todos os números ímpares entre 1 e 50.

lista = []
for i in range(51):
    if i % 2 != 0:
        lista.append(i)
print(lista)        

# O programa ler um intervalo entre 1 e 50
# no qual se o numero lido for impar ele sera adiciona em uma lista dos numeros impares
# e logo apos o programa ler todos os numeros a lista sera exibida somente com os valores impares  