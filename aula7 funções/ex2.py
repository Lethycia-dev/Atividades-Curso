def CalculoGorjeta(qtdConta):
  
    gorjetaGarcom = (qtdConta*(10/100))
    return gorjetaGarcom

gorjeta = float(input("Digite o valor da conta: "))
totalGorjeta = (CalculoGorjeta(gorjeta))

print(f"O valor da Gorjeta foi: {totalGorjeta}")

#print(f"a gorjeta foi de: {CalculoGorjeta(100)}")
   
