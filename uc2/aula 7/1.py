import psycopg2

'''
conn = psycopg2.connect(dbname = "Escola",host = "localhost",port = "5432",user = "postgres", password = "postgres")
cursor = conn.cursor()

cursor.execute('''

# SELECT * FROM "Alunos"

''')

for aluno in cursor.fetchall():
    print(f"{aluno[0]} - {aluno[1]} - {aluno[2]} - {aluno[3]} - {aluno[4]} ")

'''


try:
    conn = psycopg2.connect(dbname = "Escolaa" , host = "localhost", port = "5432", user = "postgres", password = "postgres")
    cursor = conn.cursor()


    print("Conectado com sucesso")

    
    cursor.execute ('''

        UPDATE "Alunos" 
        SET 
        "Telefone" = 'xx-xx'
       
    ''')

    conn.commit()

    conn.close()


except(Exception, psycopg2.Error) as error:
     print("Ocorreu um erro!",error)



'''
    cursor.execute('''
    
#    CREATE TABLE "Alunos" (
#        "Nro_matricula" serial, 
#        "cpf" char(11) ,
#        "Nome" varchar(255) NOT NULL,
#        "Endereço" varchar(255) default 'Não informado', 
#        "Telefone" char(11) default 'xx-xxxxx-xxxx', 
#        "Ano_Nascimento" integer,

#        PRIMARY KEY("Nro_matricula")
#    )
    
    
    #)

 #   conn.commit()
    


