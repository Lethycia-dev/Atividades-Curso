#Escreva uma função que receba como parâmetro uma lista de números inteiros e retorne a soma dos números pares na lista. Em seguida, utilize um laço de repetição para solicitar ao usuário uma lista de números inteiros, chame a função e imprima o resultado.

          
def main():
    global lista
    global listaNova
    lista = [] 
    listaNova = [] 
    for x in range(10):
        x = int(input("Digite um numero: "))
        lista.append(x)
    for i in lista:
        if i % 2 == 0:
            listaNova.append(i) 
         
    listagem()


def listagem():
  
  print("A soma dos numeros pares é: ")
  print(sum(listaNova))


  

main()