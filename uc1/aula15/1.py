class Conta:
    def __init__(self,saldo,numConta):
        self._saldo = saldo
        self._numConta = numConta

    def get_saldo(self): # ET PEGA O SALDO
        
        return self._saldo
    
    def set_saldo(self,saldo): # SET ALTERA O SALDO
       
        if saldo < 0:
            print("Saldo invalido")
            self._saldo = saldo
            
    def get_numConta(self):
        return self._numConta 
    
    def set_saldo(self,numConta):
        self._numConta = numConta   


pessoa = Conta(-140,123)
print(f"Saldo: {pessoa.get_saldo()}")        
print(f"Conta: {pessoa.get_numConta()}")        