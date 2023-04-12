import json

with open("uc2/aula4/dados2.json") as file:
    data = json.load(file)


funcionario = data['funcionarios']

for funcionario in funcionario:
    print(f"ID: {funcionario['ID']}")
    print(f"Nome: {funcionario['Nome']}")
    print(f"Salario: {funcionario['Salario']}")
    print(f"ID do Departamento: {funcionario['ID_Departamento']}")
    print("----------------------")
   
'''
with open("uc2-4/banco.json") as file:
    data = json.load(file)


funcionario = data['funcionario']

for funcionario in funcionario:
    print(f"ID: {funcionario['Id_funcionario']}")
    print(f"Nome: {funcionario['Nome']}")
    print(f"Salario: {funcionario['cpf']}")
    print(f"Departamento: {funcionario['Id_departamento']}")
    print("----------------------")
'''