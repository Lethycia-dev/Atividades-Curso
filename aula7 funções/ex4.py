'''
Faça uma função que receba uma lista de números armazenados de forma crescente, e
dois valores ( limite inferior e limite superior), e exiba a sublista cujos elementos são
maiores ou iguais ao limite inferior e menores ou iguais ao limite superior.
Exemplo:
lista inicial=[12,14,15,16,18,20,24,26,28,32,34,38]
limite inferior=13
limite superior = 26
lista exibida: [14,15,16,18,20,24,26]
'''
'''
def questaoLista():

    lista = [12,14,15,16,18,20,24,26,28,32,34,38]
    listaNova = []
    for i in lista:
        if i > 13 and i <= 26:
            listaNova.append(i)
            listaNova.sort()
            print(listaNova)
    return listaNova

print(questaoLista())
'''

def questaoLista1():
    lista1 = []
    for i in range(10):
        i = input("Digite um numero: ")
        lista1.append(i)
        print(lista1)
    return lista1

print(questaoLista1())
        
