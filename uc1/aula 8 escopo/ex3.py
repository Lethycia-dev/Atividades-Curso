# CRIAR CALCULADORA

def soma(n1,n2):
            resultado = n1 + n2
            return resultado

def subtracao(n1,n2):
            resultado = n1 - n2
            return resultado

def multiplicacao(n1,n2):
            resultado = n1 * n2
            return resultado

def divisao(n1,n2):
            if n2 == 0:
                   resultado = 0
                  
            else:
                resultado = n1 / n2
            return resultado
def main():

    num1 = float(input("digite o numero 1: "))
    operador = input("digite o operador: ")
    num2 = float(input("digite o numero 2: "))

    if operador == '+':
        print(soma(num1,num2))
    
    elif operador == '-':
        
        print(subtracao(num1,num2))   

    elif operador == '*':
        
        print(multiplicacao(num1,num2))

    elif operador == '/':
       
        print(divisao(num1,num2))

    else:
        print("Operador invalido")            


main()