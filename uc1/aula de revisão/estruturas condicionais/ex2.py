#Escreva um programa que leia o nome e a idade de uma pessoa e imprima uma mensagem personalizada com base na idade. Se a idade for menor que 18 anos, imprima "Você é menor de idade". Se a idade estiver entre 18 e 65 anos, imprima "Você é adulto". Caso contrário, imprima "Você é idoso".

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


if idade < 18 :
    print(f"{nome} você é menor de idade!")
elif 18 <= idade <= 65:
    print(f"{nome} Você é adulto")
elif idade > 65:
    print(f"{nome} Voce é idoso")
else:
    print("ERROR")          

# Programa pede que o usuario digite seu nome e sua idade e armazena em duas variaveis {nome} e {idade}
# em seguida verifica SE a idade dgitada é menor que 18 caso a afirmação seja verdadeira sera impresso na tela que o usuario é menor de idade
# senao se a idade digitada estiver entre 18 incluindo o 18 e entre 65 incluindo o 65, sera impresso que o usuario é adulto 
# senao se a idade digitada for maior que 65 sera impresso que o usuario é idoso
# senao o programa imprimirá ERROR pois digitou a idade errada       