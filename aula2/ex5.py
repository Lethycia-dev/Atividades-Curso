nomeAluno = input("Nome do aluno: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media = (nota1 + nota2 + nota3) / 3
mediaTexto = "{0:.2f}".format(media)
print(mediaTexto)

if media >= 7:
    print("Aluno Aprovado")
elif media <= 5:
    print("Aluno Reprovado")
else:
    print("Aluno em Recuperação")        
