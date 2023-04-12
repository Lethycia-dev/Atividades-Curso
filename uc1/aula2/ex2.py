valorA = int(input("Digite o valor A:"))
valorB = int(input("Digite o valor B:"))
valorC = int(input("Digite o valor C:"))
resultado = int(valorA + valorB)


if resultado < valorC:
    print(f"{resultado} é menor que {valorC}")
else:
    print(f"{resultado} é maior que {valorC}")    