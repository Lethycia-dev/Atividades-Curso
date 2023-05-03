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
     input("Enter...")


def inserirLivro():
     
     livro = Livros(None,input("Digite o nome do livro: "),input("Digite o nome do Autor: "))
     conexaoLivros.alterarLivros(livro.cadastrarLivro())

     print("Livro cadastrado com sucesso!") 
     input("Enter...")

def inserirAluguel():
    
    
     aluguel = Alugueis(None,input(f"Digite o ID do Livro: "),input(f"Digite o ID do Cliente: "),None,input("Devolução: "))
     conexaoLivros.alterarLivros(aluguel.cadastrarAluguel())

     print("Aluguel cadastrado com sucesso!")
     input("Enter...")

def verListaLivros():

    listaLivros = conexaoLivros.consultaLivros('''
    
    SELECT * FROM "Livros"
    
    ''')
    for livro in listaLivros:
         print(f'''
         ID - {livro[0]}
         Nome - {livro[1]}
         Autor - {livro[2]}
         
         ''')
    input("Enter...")
     

def verListaClientes():

    listaClientes = conexaoLivros.consultaClientes('''
    
    SELECT * FROM "Clientes"
   
    ''')  

    for cliente in listaClientes:
         print(f'''
          ID - {cliente[0]}
          Nome - {cliente[1]}
         
         ''')

    input("Enter...")

def verListaAlugueis():
    

    listaAlugueis = conexaoLivros.consultaLivros('''
    
    SELECT * FROM "Alugueis"
    
    ''')

    for aluguel in listaAlugueis:
         livro = conexaoLivros.consultaLivros(f'''
         
            SELECT * FROM "Livros"
            WHERE
            "Id_Livro" = {aluguel[1]}
         
         ''')[0]

         cliente = conexaoLivros.consultaLivros(f'''
         
            SELECT * FROM "Clientes"
            WHERE
            "Id_Cliente" = {aluguel[2]}
         
         ''')[0]

         print(f'''
         ID Aluguel- {aluguel[0]}
         ID Livro - {aluguel[1]}
         Nome Livro - {livro[1]}
         ID Cliente - {aluguel[2]}
         Nome Cliente - {cliente[1]}
         Data de Aluguel - {aluguel[3]}
         Data de Entrega - {aluguel[4]}

         ''')

    input("Enter...")    

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

     # conexaoLivros.alterarLivros('''
     
     # DELETE FROM 
     #      "Alugueis"
     #      WHERE
     #      "Id_Aluguel" = 3
     
     # ''')
     # print("deletado!")



    while True:
         print('''
         
            Menu:
            1 - Ver Livros
            2 - Ver Clientes
            3 - Ver Alugueis
            4 - Cadastrar Livro
            5 - Cadastrar Cliente
            6 - Cadastrar Aluguel
            0 - Sair

         ''')
         op = input("Digite uma opção: ")

         match op:
               case "1": 
                   verListaLivros()
               
               case "2": 
                   verListaClientes()
              
               case "3": 
                   verListaAlugueis()

               case "4": 
                   inserirLivro()
              
               case "5": 
                   inserirCliente()
    
               case "6": 
                   inserirAluguel()

               case "0":
                   print("Saindo...")
                   break         

except(Exception,psycopg2.Error) as error:
     print("Ocorreu um erro: ", error)       




