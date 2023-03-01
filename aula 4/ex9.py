palavra = str(input("Digite uma palavra: "))

for i in range(len(palavra)):
   if i % 2 == 0:
      print(f"{i+1} {palavra[i]}")
        