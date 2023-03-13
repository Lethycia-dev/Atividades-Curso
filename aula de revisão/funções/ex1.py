#Escreva uma função que receba uma lista de números inteiros e retorne o maior número da lista.

def main():
    global lista 
    lista = [3,4,8,5,6,98,7,8,4,1,25,31,10,25,14,15,69,48,47,11,20,33]
    numerosMaior()

def numerosMaior():
    
    print(max(lista))

main()
