class Alugueis:
    def __init__(self,id_aluguel,id_livro,id_cliente,time,devolução):
        self._id_aluguel = id_aluguel
        self._id_livro = id_livro
        self._id_cliente = id_cliente
        self._time = time
        self._devolução = devolução

    def cadastrarAluguel(self):

        sql = f'''
        
        INSERT INTO "Alugueis"
        VALUES (default,'{self._id_livro}','{self._id_cliente}',default,'{self._devolução}')
        
        '''
        
        return sql