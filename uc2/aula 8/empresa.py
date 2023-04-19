import psycopg2

'''
def criarTabelaFuncionario():
    
    sql = 
    
    CREATE TABLE "Funcionarios" (
    
        "Id_Func" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        "Nome_Func" char (255) NOT NULL,
        "Salario_Func" float(2) NOT NULL default 0.00,
        "Cargo_Func" char (255) NOT NULL default 'Autonomo',
        "Id_Departamento" integer 

    )    
    
    return sql


def criarTabelaDepartamento():
    
    sql = 
    
CREATE TABLE "Departamentos" (
    
        "Id_Dep" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        "Nome_Dep" char (255) NOT NULL
        
    )    
#    return sql


try:

    conn = psycopg2.connect(dbname = "Empresa", host = "localhost", port = "5432", user = "postgres", password = "postgres")
    cursor = conn.cursor()

    cursor.execute (criarTabelaFuncionario())
    conn.commit()

    cursor.execute (criarTabelaDepartamento())
    conn.commit()

    print("Tabelas criadas")
    conn.close()
    

except(Exception,psycopg2.Error) as error:
    print("Ocorreu um erro: ", error)
'''

def verFuncionarios():
    cursor.execute('''
    
    SELECT * FROM "Funcionarios"
    ORDER BY "Id_Func"  ASC    
    '''
    )

    listaFuncionarios = cursor.fetchall()
    for funcionario in listaFuncionarios:
        print("ID - NOME - SALARIO - CARGO - DEPARTAMENTO ")
        print(f"{funcionario[0]} - {funcionario[1]} - {funcionario[2]} - {funcionario[3]} - {funcionario[4]}")
        print("--------------")

    input("Enter...")

def verDepartamento():
    
    cursor.execute('''
    
    SELECT * FROM "Departamentos"
    ORDER BY "Id_Dep"  ASC      
    '''
    )

    listaDepartamentos = cursor.fetchall()
    print(listaDepartamentos)
    
    input("Enter...")

def inserirFuncionario():
    print("Cadastro de novo funcionario...")

    nomeFunc = input("Digite o nome do Funcionario: ")
    salarioFunc = input("Digite o salario do Funcionario: ")
    cargoFunc = input("Digite o cargo do Funcionario: ")
    id_Dep = input("Digite o id do Departamento: ")

    cursor.execute(f'''
    
    INSERT INTO "Funcionarios"
    VALUES(default, '{nomeFunc}', '{salarioFunc}','{cargoFunc}','{id_Dep}')
    '''
    )

    conn.commit()
    print("Funcionario inserido com sucesso!")

    input("Enter...")

def inserirDepartamento():

    nomeDep = input("Digite o nome do Departamento: ")

    cursor.execute(f'''
    
    INSERT INTO "Departamentos"
    VALUES(default,'{nomeDep}')
    
    '''
    )
    conn.commit()
    print("Departamento inserido com sucesso")

    input("Enter...")
try:

    conn = psycopg2.connect(dbname = "Empresa", host = "localhost", port = "5432", user = "postgres", password = "postgres")
    cursor = conn.cursor()

    print("Conexão Efetuada")


    while True:
        print('''
        
        Menu:

        1 - Ver Funcionarios
        2 - Ver Departamentos
        3 - Inserir Funcionario
        4 - Inserir Departamento
        0 - Sair
        

        ''')

        op = input("Digite um opção: ")

        match op:

            case "1": 
                verFuncionarios()
            
            case "2": 
                verDepartamento()
            
            case "3": 
                inserirFuncionario()
            
            case "4": 
                inserirDepartamento()
            
            case "0": 
                print("Saindo...")
                cursor.close()
                conn.close()
                break                


except(Exception,psycopg2.Error) as error:
    print("Ocorreu um erro: ", error)


































