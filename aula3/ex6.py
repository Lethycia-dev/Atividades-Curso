num1 = input("Digite um numero inteiro: ")
num2 = input("Digite um numero inteiro: ")
num3 = input("Digite um numero inteiro: ")

primeiro = None
segundo = None
terceiro = None


if (num1 != num2 and num1 != num3 and num2 != num3):
    if (num1 > num2 and num1 > num3):
        primeiro = num1
    elif (num2 > num1 and num2 > num3):
        primeiro = num2        