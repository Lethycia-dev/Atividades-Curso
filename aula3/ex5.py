# PRIMO OU NÃO

while True:
    num = int(input("Digite um numero: "))

    if num == 0:
        break
    elif num % 2 != 0:
        print(f"{num} é um numero primo")
    elif num % 2 == 0:
        print(f"{num} não é um numero primo")
    else:
        print("NaN")
   
'''
numero = int(input("Digite um numero inteiro: "))

contador = 0

for i in range(1,numero + 1):
    if numero % i == 0:
        contador = contador + 1 
        print(contador, "-",i)

if contador <= 2:
    print(f"{numero} Numero primo")
else:
    print(f"{numero} Não é primo")    
'''    