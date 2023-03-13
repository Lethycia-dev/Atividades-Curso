#Escreva um programa que leia uma lista de números inteiros e remova todos os valores duplicados. Em seguida, imprima a lista sem os valores duplicados.

lista = [1,1,2,2,3,3,4,5,6,7,8,9,10,15,48,7,9,3,10]
listaNova = []
for i in lista:
    if i not in listaNova:
        listaNova.append(i)
        

print(listaNova)    

#O programa tem definida uma lista na qual exibe numeros repetidos
# é criado uma nova lista vazia 
# é criado uma estrutura de repetição para percorrer toda a lista 
# se o numero verificado não estiver dentro da lista nova criada ,o programa adicionara o elemento na nova lista 
# se ele ja estiver o programa passará para o proximo elemento afimj de achar elementos não repetidos
# ao fim ele imprime a nova lista com os numeros sem repetições 