'''
lista = ['abc','xyz','aba','1221']
textos = 0
x = int(0)
comparacao1 = lista[0][0]
comparacao2 = lista[0][-1]


for x in lista:

    if comparacao1 == comparacao2 and len(lista) >= 2:
        
        textos = textos + 1
    else:
        x = (x + 1)    
        comparacao1 = lista[x][0]
        comparacao2 = lista[x][-1]
 
   
        
            

print(textos)         
'''
lista = ['abc','xyz','aba','1221']

contador = 0

for termo in lista:

    if len(termo) >= 2:
        if termo[0] == termo[-1]:
            contador += 1

print(contador)            

