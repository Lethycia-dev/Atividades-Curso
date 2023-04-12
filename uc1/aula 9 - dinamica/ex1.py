'''
Q.1 Construa um algoritmo para ler um número inteiro, positivo de três dígitos, e gerar outro número formado pelos dígitos invertidos do número lido. 
 Ex: 
NumeroLido = 123 
NumeroGerado = 321 
Dica: Observe os resultados das funções Quociente e Resto de um número por 10. 


'''


def main():

    while True:
        global num
        num = input("Digite um numero inteiro: ")
   

        if len(num) == 3:
            reverso()
            print(reverso()[::-1])
            break

        elif len(num) < 3:
            print("Digite um numero inteiro com 3 digitos")
            
        
        else:
            print("Digite um numero inteiro com 3 digitos")
            


def reverso():
    
    lista = []
    lista.append(num)
    
    return num
    
    

main()


