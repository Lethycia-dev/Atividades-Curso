
palavra = input("Digite uma palavra: ") ## [::-1]INVERTE UMA PALAVRA AO CONTRARIO 

print((palavra)[::-1])

palavraInvertida = ""

for i in range(len(palavra)):
    palavraInvertida = palavraInvertida + palavra[len(palavra)-1-i] 
    print(palavraInvertida)





