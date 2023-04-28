import psycopg2
from controle.classConexao import Conexao




class Livros:
    def __init__(self,id,nome,autor):
        self._id = id
        self._nome = nome
        self._autor = autor

    def cadastrarLivro(self):

        sql = '''
        
        INSERT INTO "Livros"
        VALUES (default,'{self._nome}','{self._autor}') 
         
        '''
        return sql
    
   
           