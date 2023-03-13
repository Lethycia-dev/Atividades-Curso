def potencia(base, expoente):
    resultado = 1
    for i in range(expoente):
        resultado *= base
        return resultado
    
print(potencia(base = 10, expoente = 5))    
        
