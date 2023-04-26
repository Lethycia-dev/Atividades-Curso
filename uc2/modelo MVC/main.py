from controle.classConexao import Conexao
import psycopg2


conexaoBanco = Conexao("Mercado","localhost","5432","postgres","postgres")

try:
    # conexaoBanco.manipularBanco('''
    
    # CREATE TABLE "Cliente" (
    # "Id_Cliente" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    # "Nome_Cliente" varchar(255)
    # )
    # '''     
    # )

    # print("tabela criada")

    conexaoBanco.manipularBanco('''
    
    CREATE TABLE "Compra" (
    "Id_Compra" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Id_Cliente" int,
            CONSTRAINT fk_ID_Cliente
                FOREIGN KEY ("Id_Cliente")
                REFERENCES "Cliente"("Id_Cliente")
                 ON DELETE NO ACTION
                 ON UPDATE NO ACTION,
    "Id_Produto" int,
            CONSTRAINT fk_Id_Produto
                FOREIGN KEY ("Id_Produto")
                REFERENCES "Produto"("Id_Produto")
                 ON DELETE NO ACTION
                 ON UPDATE NO ACTION,

    "Quantidade" int,
    "Valor Total"  numeric, 
    "Timestamp" timestamp default CURRENT_TIMESTAMP(0)                       
    )
    '''     
    )
    print("tabela criada")

    # conexaoBanco.manipularBanco('''
    
    # CREATE TABLE "Produto" (
    # "Id_Produto" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    # "Nome_Produto" varchar(255),
    # "Preço_Produto" numeric,
    # "Estoque_Produto" int
    # )
    
    
    # ''')



    # print("tabela criada")
   
    
except(Exception,psycopg2.Error) as error:
     print("Ocorreu um erro: ", error)   