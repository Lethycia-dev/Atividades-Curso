'''
Escreva um programa Python para obter uma lista, classificada em ordem crescente pelo último elemento em cada tupla de uma determinada lista de tuplas não vazias. Ir para o editor
Lista de amostras: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] Resultado esperado: [(2, 1), (1 , 2), (2, 3), (4, 4), (2, 5)]
'''
'''

def questao6():

    lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

    novaLista = []

    listaPosicoes = []
'''
lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

novaLista = []

for tupla in lista:

    novaLista.append(tupla[::-1])
novaLista.sort()

lista.clear()

for tupla in novaLista:

    lista.append(tupla[::-1])

print(lista)
