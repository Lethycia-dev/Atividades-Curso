import psycopg2

sql = ('''
CREATE TABLE Teste 
Id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome varchar (255) NOT NULL,
telefone numeric ()

''') 

sql = ('''

DROP TABLE Teste

''')

sql = ('''

ALTER TABLE Teste
ADD cpf numeric (11)
''')

sql = ('''

UPDATE Teste
SET 
"Nome" = {novo}
WHERE
"Id" = {id}

''')
sql = ('''

SELECT * FROM "Teste"

''')

sql = ('''

INSERT INTO "Teste"
VALUES(default,{nome},{telefone})

''')
sql = ('''

DELETE FROM "Teste"
WHERE "Id" = {id}

''')


