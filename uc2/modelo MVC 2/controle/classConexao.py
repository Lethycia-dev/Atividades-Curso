import psycopg2


class Conexao:
    def __init__(self,dbname,host,port,user,password):
        self._dbname = dbname
        self._host = host
        self._port = port
        self._user = user
        self._password = password


    def consultaLivros(self,sql):
        conn = psycopg2.connect(dbname = self._dbname,host = self._host,port = self._port,user = self._user,password = self._password)
        cursor = conn.cursor()

        listaLivros = cursor.fetchall()

        cursor.close()
        conn.close()

        return listaLivros
    
    def consultaClientes(self,sql):
        conn = psycopg2.connect(dbname = self._dbname,host = self._host,port = self._port,user = self._user,password = self._password)
        cursor = conn.cursor()

        listaClientes = cursor.fetchall()

        cursor.close()
        conn.close()

        return listaClientes


    def alterarLivros(self,sql):

        conn = psycopg2.connect(dbname = self._dbname,host = self._host,port = self._port,user = self._user,password = self._password)
        cursor = conn.cursor()

        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()