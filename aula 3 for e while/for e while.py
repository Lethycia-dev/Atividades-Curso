# USO DO FOR
nomes = ['Pedro', 'João', 'Lethycia']

for n in nomes:
    print(n)

# USO DO WHILE 

contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1   

while True:
    cpf = input("Digite seu CPF: ")

    if len(cpf) != 11:
        print ("Seu CPF deve ter 11 digitos")
    else:
        break    
