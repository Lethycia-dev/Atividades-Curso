import psycopg2


# def criarTabelaFuncionarios():
#     sql = '''
#         CREATE TABLE "Funcionarios"(
#            "Func_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#             "Func_nome"  varchar(255),
#             "Func_cpf"  char(11) NOT NULL,
#             "Func_salario"  money,
#             "Id_Departamento"  int,
#             CONSTRAINT fk_Departamento
#                 FOREIGN KEY ("Id_Departamento")
#                 REFERENCES "Departamentos"("Id_Dept")  
#                 ON DELETE NO ACTION
#                 ON UPDATE NO ACTION
#                 )''' 
#     return sql

# def criarTabelaDepartamentos():    
#     sql = '''
#             CREATE TABLE "Departamentos" (
        
#             "Id_Dept" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#             "Nome_Dep" char (255) NOT NULL
#             )'''
#     return sql

# try:

#     conn = psycopg2.connect(dbname = "Empresa2", host = "localhost", port = "5432", user = "postgres", password = "postgres")
#     cursor = conn.cursor()

#     cursor.execute (criarTabelaDepartamentos())
#     conn.commit()

#     cursor.execute (criarTabelaFuncionarios())
#     conn.commit()

#     print("Tabelas criadas")
#     conn.close()

# except(Exception,psycopg2.Error) as error:
#     print("Ocorreu um erro: ", error)

try:

        conn = psycopg2.connect(dbname = "Empresa2", host = "localhost", port = "5432", user = "postgres", password = "postgres")
        cursor = conn.cursor()


        # cursor.execute ('''
        # INSERT INTO "Departamentos"
        # VALUES(default,'Vendas'),
        # (default,'Comercial')

        
        # ''')
   
        # conn.commit()

        cursor.execute ('''
        INSERT INTO "Funcionarios"
        VALUES (default,'Maria Joaquina',12345,2000,2),
        (default,'Cirilo',1234,4000,2),
        (default,'Alicia',12345,7000,2)
              
        ''')
        conn.commit()

        print("Tudo certo...")
        conn.close()

except(Exception,psycopg2.Error) as error:
     print("Ocorreu um erro: ", error)