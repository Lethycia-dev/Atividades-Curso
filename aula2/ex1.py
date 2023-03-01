idade = int(input("Digite a sua idade: "))

check1 = idade >= 10 and idade < 20
check2 = idade >= 20 and idade < 30
check3 = idade >= 30 and idade <= 100

print(check1,check2,check3)

if check1:
    print("Você é adolescente")

elif check2:

    print("Você é jovem")

elif check3:
    print("Você é adulto")

else:
    print("Valor não encontrado")        


