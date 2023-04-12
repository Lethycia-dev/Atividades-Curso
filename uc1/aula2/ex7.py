# QUESTÃO DOS SANDUICHES

print('''
100 Cachorro quente: 1,10
101 Bauru simples: 1,30
102 Bauru c/ovo: 1,50
103 Hamburger: 1,10
104 Cheeseburger: 1,30
105 Refrigerante: 1,00
''')

codigo = input("Digite o codigo do seu pedido: ")


if (codigo >= '100' and codigo <= '105'):
    quantidade = int(input("Digite a quantidade do seu pedido: "))

    if codigo == '100':
        nome = 'Cachorro quente'
        preco = 1.10
    elif codigo == '101':
        nome = 'Bauru Simples'
        preco = 1.30    
    elif codigo == '102':
        
        nome = 'Bauru com ovo'
        preco = 1.50
    elif codigo == '103':
        nome = 'Hamburguer'
        preco = 1.10
    elif codigo == '104':
        nome = 'Cheeseburguer'
        preco = 1.30
    elif codigo == '105':
        nome = 'Refrigerante'

        preco = 1.00

    precoTotal = quantidade * preco

    print(f"O seu pedido de {quantidade} {nome} deu o valor de R$: {precoTotal}")

else:
    print("Codigo invalido")


