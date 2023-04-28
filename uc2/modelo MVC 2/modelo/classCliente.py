from controle.classConexao import Conexao


class Cliente:
    def __init__(self,id,nome):
        self._id = id
        self._nome = nome

    def cadastrarCliente(self):
        sql = '''
        
        INSERT INTO "Clientes"
        VALUES (default,'{self._nome}')
       
        '''
        return sql
     
    
