import json



with open("funcionario.json",'r') as funcionariosJson:
    listaFuncionarios = json.load(funcionariosJson)

def vizualizarFuncionarios():
    
    print(listaFuncionarios)


def cadastrarFuncionario():
    funcionario = {}
    nomeFunc = input("Digite o nome do Funcionario: ")    
    salarioFunc = float(input("Digite o nome do Funcionario: "))    
    cargoFunc = input("Digite o nome do Funcionario: ")    
    cpfFunc = input("Digite o nome do Funcionario: ")    
    departamentoFunc = input("Digite o nome do Funcionario: ")

    funcionario["nome"] = nomeFunc
    funcionario["salario"] = salarioFunc
    funcionario["cargo"] = cargoFunc
    funcionario["cpf"] = cpfFunc
    funcionario["departamento"] = departamentoFunc

    listaFuncionarios.append(funcionario)
    return listaFuncionarios



while True:
    
    print('''

    Menu:

    1.Visualizar Funcionarios 
    2.Cadastrar Funcionario 
    3. Sair

    ''')    
    
    op = input("Digite a opção escolhida: ")

    match op:
        case "1":
            print(f"A lista de Funcionarios é: {listaFuncionarios}")
        case "2":
            cadastrarFuncionario()
        case "3":
            print("Sair do programa")
            break       


