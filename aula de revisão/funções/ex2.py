#Escreva uma função que receba uma lista de números inteiros e retorne a soma dos números pares da lista.

def main():
    global lista
    global listaNova
    listaNova = []
    lista = [5,8,9,6,12,45,78,94,10,32,25,62,13,0,54,78,95,11]
    for i in lista:
        if i % 2 == 0:
            listaNova.append(i)
    soma()

def soma():
    
    print(sum(listaNova))
        
main()        