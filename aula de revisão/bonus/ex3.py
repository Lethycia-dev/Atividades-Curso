#Escreva uma função que receba como parâmetro uma lista de strings e retorne a quantidade de strings que possuem mais de 5 caracteres. Em seguida, utilize uma estrutura condicional para perguntar ao usuário se ele deseja adicionar mais strings à lista, e utilize um laço de repetição para solicitar ao usuário as novas strings, chame a função e imprima o resultado.

def main():
    global lista
    lista = ['le','thy','cia','may','ra','abcdef','ahsgahsga','asjajhdkjhdsjkhd']
    for i in len(lista):
        if len(i) >= 5:
            print(i)

main()            