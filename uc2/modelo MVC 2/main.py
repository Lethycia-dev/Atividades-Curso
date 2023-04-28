from controle.classConexao import Conexao
from modelo.classCliente import Cliente
from modelo.classLivros import Livros
from modelo.classAlugueis import Alugueis

import psycopg2


conexaoLivros = Conexao("Biblioteca","localhost","5432","postgres","postgres" )

def inserirCliente():
     
     cliente = Cliente(None,input("Digite o nome do cliente: "))
     conexaoLivros.alterarLivros(cliente.cadastrarCliente())

     print("Cliente cadastrado com sucesso!") 


def inserirLivro():
     
     livro = Livros(None,input("Digite o nome do cliente: "),input("Digite o nome do Autor: "))
     conexaoLivros.alterarLivros(livro.cadastrarLivro())

     print("Livro cadastrado com sucesso!") 

def inserirAluguel():
     
    aluguel = Alugueis(None,None,None)
    conexaoLivros.alterarLivros(aluguel.cadastrarAluguel())

    print("Aluguel cadastrado com sucesso!")

def verListaLivros():

    conexaoLivros.consultaLivros('''
    
    SELECT * FROM "Livros"
    ORDER BY "Id" ASC
    
    ''')


def verListaClientes():

    conexaoLivros.consultaClientes('''
    
    SELECT * FROM "Clientes"
    ORDER BY "Id" ASC
    
    ''') 


try:
    # conexaoLivros.alterarLivros('''
    
    # CREATE TABLE "Clientes" (
    # "Id_Cliente" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    # "Nome_Cliente" varchar(255) NOT NULL
    # )
    # ''')

    # conexaoLivros.alterarLivros('''
    
    # CREATE TABLE "Livros" (
    # "Id_Livro" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    # "Nome_Livro" varchar(255) NOT NULL,
    # "Autor_Livro" varchar(255) default 'Desconhecido'

    # )            
    # ''')

    # conexaoLivros.alterarLivros('''
    
    # CREATE TABLE "Alugueis" (
    # "Id_Aluguel" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    # "Id_Livro" int,
    #     CONSTRAINT fk_id_livro
    #         FOREIGN KEY ("Id_Livro")
    #         REFERENCES "Livros"("Id_Livro"),

    # "Id_Cliente" int,
    #     CONSTRAINT fk_id_cliente
    #         FOREIGN KEY ("Id_Cliente")
    #         REFERENCES "Clientes"("Id_Cliente"),

    # "Data_Aluguel" timestamp default CURRENT_TIMESTAMP(0),
    # "Devolução_Aluguel" timestamp
    #     )
    # ''')

    # print("Tabelas criadas!!")


    # conexaoLivros.alterarLivros('''
    
    # INSERT INTO "Clientes"
    # VALUES(default,'Lethycia'),
    # (default,'Mayra'),
    # (default,'Jose')
    
       
    # ''')
    # print("Clientes cadastrados!")

    while True:
         print('''
         
            Menu:
            1 - Ver Livros
            2 - Ver Clientes
            3 - Cadastrar Livro
            4 - Cadastrar Cliente
            5 - Cadastrar Aluguel
            0 - Sair

         ''')
         op = input("Digite uma opção: ")

         match op:
              case "1": 
                   verListaLivros()
               
              case "2": 
                   verListaClientes()
              
              case "3": 
                   inserirLivro()
              
              case "4": 
                   inserirCliente()
    
              case "5": 
                   inserirAluguel()

              case "0":
                   print("Saindo...")
                   break         

except(Exception,psycopg2.Error) as error:
     print("Ocorreu um erro: ", error)       




