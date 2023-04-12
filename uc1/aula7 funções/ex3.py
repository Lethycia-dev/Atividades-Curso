

def contadorDeString(palavra,letra):

    contador = 0

    for l in palavra:
        if l.lower == letra.lower:
            contador += 1
    return contador

palavras = input("digite uma palavra: ")
letra = input("Digite a letra: ")
letraTotal = contadorDeString(palavras,letra)
print(f" {letraTotal}")




#Crie uma função que permita contar o número de vezes que aparece uma letra em uma
#string.
'''
def contaLetras(palavra,letra):
    contador = 0
    for l in palavra:
        if l.lower() == letra.lower():
            contador += 1
    return contador

pal = input("Digite uma palavra: ")
let = input("Digite uma letra: ")

contagem = contaLetras(pal, let)
contagem1 = pal.count(let)

print(f"A letra {let} aparece {contagem}x na {pal}")
print(contagem1)

'''