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
    ORDER BY "Id_Livro" ASC
    
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
    ORDER BY "Id_Cliente" ASC
   
    ''')  

    for cliente in listaClientes:
         print(f'''
          ID - {cliente[0]}
          Nome - {cliente[1]}
         
         ''')


    verClienteEspecifico()         

def verClienteEspecifico():
    
    clienteEspecifico = input("Ver informações especificas de um cliente? S/N ")

    if clienteEspecifico.upper == "S" or clienteEspecifico == "s":
            
            idEspecifico = input("Digite o ID do Cliente que deseja ver mais informações: ")

            cliente = conexaoLivros.consultaClientes(f'''
            SELECT * FROM "Clientes"
            WHERE "Id_Cliente" = {idEspecifico}
            ''')

            print(f"Cliente escolhido: {cliente[1]}")
            
            listaAlugueis = conexaoLivros.consultaAlugueis(f'''
            
            SELECT * FROM "Alugueis" 
            WHERE "Id_Cliente" = {idEspecifico}
            
            ''')
            if listaAlugueis:
              for aluguel in listaAlugueis:
                clientedoAluguel = conexaoLivros.consultaAlugueis(f'''
                SELECT * FROM "Alugueis"
                WHERE "Id_Cliente" = {aluguel[0]}
                
                ''')[0]
                livroDoAluguel = conexaoLivros.consultaLivros(f'''
                
                SELECT * FROM "Livros"
                WHERE "Id_Livro" = {aluguel[0]}
                
                ''')[0]

            print(f'''
                 Cliente: {clientedoAluguel[0]}
                 Cliente: {livroDoAluguel[1]}
                 livros: {aluguel[0]}
                 livros: {aluguel[3]}
                    
                    ''')  

    else:
        input("Enter...") 

def verListaAlugueis():
    

    listaAlugueis = conexaoLivros.consultaLivros('''
    
    SELECT * FROM "Alugueis"
    ORDER BY "Id_Aluguel" ASC
    
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

def deletarLivro():

    verListaLivros()
     
    apagarLivro = input("Digite o id do Livro que deseja apagar: ")

    conexaoLivros.alterarLivros(f'''
     
     DELETE FROM 
           "Livros"
           WHERE
           "Id_Livro" = {apagarLivro}
         
     ''')
    print("Livro Deletado com Sucesso!")
    input("Enter...")
    

def deletarCliente():

    verListaClientes()
     
    apagarCliente = input("Digite o id do Cliente que deseja apagar: ")

    conexaoLivros.alterarLivros(f'''
     
     DELETE FROM 
           "Clientes"
           WHERE
           "Id_Cliente" = {apagarCliente}
         
     ''')
    
    print("Cliente Deletado com Sucesso!")
    input("Enter...")

def deletarAluguel():

    verListaAlugueis()
     
    apagarAluguel = input("Digite o id do Aluguel que deseja apagar: ")

    conexaoLivros.alterarLivros(f'''
     
     DELETE FROM 
           "Alugueis"
           WHERE
           "Id_Aluguel" = {apagarAluguel}
         
     ''')  
    print("Aluguel Deletado com Sucesso!")
    input("Enter...")

def atualizarCliente():

    verListaClientes()

    idEspecifico = input("Digite o id do Cliente que deseja atualizar: ")
    novoNome = input("Digite o nome do Cliente: ")

    conexaoLivros.alterarLivros(f'''
    
    UPDATE "Clientes"
    SET 
    "Nome_Cliente" = '{novoNome}'
    WHERE
    "Id_Cliente" = {idEspecifico}
    
    ''')
    print("Cliente Atualizado com Sucesso!")
    input("Enter...")    


def atualizarLivro():

    verListaLivros()

    idLivro = input("Digite o id do Livro que deseja atualizar: ")
    novoNomeLivro = input("Digite o novo nome do Livro: ")
    novoNomeAutor = input("Digite o novo nome do Autor: ")

    conexaoLivros.alterarLivros(f'''
    
    UPDATE "Livros"
    SET
    "Nome_Livro" = '{novoNomeLivro}',
    "Autor_Livro" = '{novoNomeAutor}'
    WHERE 
    "Id_Livro" = {idLivro}
    
    ''')
    print("Livro Atualizado com Sucesso!")
    input("Enter...")

def atualizarAluguel():

    verListaAlugueis()

    idAluguel = input("Digite o ID do Aluguel que deseja atualizar: ")
    novoIdLivro = input("Digite o ID do livro: ")
    novoIdCliente = input("Digite o ID do Cliente: ")
    novaDevolucao = input("Digite a nova data de entrega: ")

    conexaoLivros.alterarLivros(f'''
    
    UPDATE "Alugueis"
    SET 
    "Id_Livro" = {novoIdLivro},
    "Id_Cliente" = {novoIdCliente},
    "Devolução_Aluguel" = {novaDevolucao}
    WHERE 
    "Id_Aluguel" = {idAluguel}
    
    
    ''')
    print("Aluguel Atualizado com Sucesso!")
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
            1 - Menu Livros
            2 - Menu Clientes
            3 - Menu Alugueis
            0 - Sair do Programa

         ''')
         op = input("Digite uma opção: ")

         match op:
               case "1": 
                   
                   print('''
                   
                   Menu livros:
                   1 - Ver Livros
                   2 - Cadastrar Livro
                   3 - Deletar Livro
                   4 - Atualizar Livro
                   0 - Voltar ao Menu Principal
                   ''')
                 

                   op = input("Digite uma opção: ") 

                   match op:
                        case "1":
                           verListaLivros()
                        case "2":
                           inserirLivro()
                        case "3":
                           deletarLivro()
                        case "4":
                           atualizarLivro()       
                        case "0":
                           print("Voltando ao menu principal...") 
                           breakpoint        
               
               case "2": 
                   print('''
                   
                   Menu Clientes:
                   1 - Ver Clientes
                   2 - Cadastrar Cliente
                   3 - Deletar Cliente
                   4 - Atualizar Cliente
                   0 - Voltar ao Menu Principal                   
                   ''')
                   


                   op = input("Digite uma opção: ")

                   match op:
                       case "1":
                           verListaClientes()
                       case "2":
                           inserirCliente()
                       case "3":
                           deletarCliente()
                       case "4":
                           atualizarCliente()       
                       case "0":
                           print("Voltando ao Menu Principal...")
                           breakpoint               
              
               case "3": 
                   print('''
                   
                    Menu Alugueis:

                    1 - Ver Alugueis
                    2 - Cadastrar Aluguel
                    3 - Deletar Aluguel
                    4 - Atualizar Aluguel
                    0 - Voltar ao Menu Principal

                   ''')


                   op = input("Digite uma opção: ")

                   match op:
                       case "1":
                           verListaAlugueis()
                       case "2":
                           inserirAluguel()
                       case "3":
                            deletarAluguel()
                       case "4":
                           atualizarAluguel()        
                       case "0":
                           print("Voltando ao Menu Principal...")
                           breakpoint          
               case "0":
                 print("Saindo do Programa...")
                 break   
              
                     

except(Exception,psycopg2.Error) as error:
     print("Ocorreu um erro: ", error)       




