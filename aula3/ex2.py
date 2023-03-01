numeros = 0
quantidade = 0
for i in range(10):
    numeros = int(input("Insira um numero: "))
  
    if numeros >= 10 and numeros <= 50:
        quantidade = quantidade + 1
    
print(f"A quantidade de numeros no intervalo foi: {quantidade}")
