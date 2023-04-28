class Alugueis:
    def __init__(self,id_aluguel,id_livro,id_cliente):
        self._id_aluguel = id_aluguel
        self._id_livro = id_livro
        self._id_cliente = id_cliente

    def cadastrarAluguel(self):

        sql = '''
        
        INSERT INTO "Alugueis"
        VALUES (default,default,default)
        
        '''
        
        return sql