'''
1. Classe Triangulo: Crie uma classe que modele um triangulo:
    Atributos: LadoA, LadoB, LadoC
   Métodos: calcular Perímetro, getMaiorLado;
Crie um programa que uFlize esta classe. Ele deve pedir ao usuário que informe as
medidas de um triangulo. Depois, deve criar um objeto com as medidas e imprimir
sua área e maior lado.
'''
'''
class Triangulo:
    def __init__(self, ladoA,ladoB,ladoC):
        self.ladoA = int(input("digite o lado A do trinagulo"))
        self.ladoB = int(input("digite o lado B do trinagulo"))
        self.ladoC = int(input("digite o lado C do trinagulo"))

    def calcularPerimetro(self,ladoA,ladoB,ladoC,perimetro):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        self.perimetro = ladoA + ladoB + ladoC
        print("O perimetro é de ", perimetro)
        return perimetro

    def maiorLado(self, ladoA,ladoB,ladoC,maior):
        if ladoA > ladoB and ladoA > ladoC:
            self.maior = ladoA
        elif ladoB > ladoA and ladoB > ladoC:
            self.maior = ladoB
        else:
            self.maior = ladoC    
        print("O maior lado é :",maior)    
'''
class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA 
        self.ladoB = ladoB 
        self.ladoC = ladoC

    def calcularPerimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro 
    def getMaiorLado(self):
        
        maior = self.ladoA
        if self.ladoB > maior and self.ladoB > self.ladoC:
            maior = self.ladoB

        elif self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            maior = self.ladoA
        
        elif self.ladoC > self.ladoB and self.ladoC > self.ladoA:
            maior = self.ladoC

        return maior    
    
lado1 = float(input("Digite o lado A do triangulo: "))    
lado2 = float(input("Digite o lado B do triangulo: "))    
lado3 = float(input("Digite o lado C do triangulo: "))    

triangulo1 = Triangulo(lado1,lado2,lado3)

print("perimetro é: ",triangulo1.calcularPerimetro)
print("maior lado é: ",triangulo1.getMaiorLado)