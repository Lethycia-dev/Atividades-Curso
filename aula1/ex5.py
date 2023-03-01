# EXERCICIO DE DICIONARIO 

pessoa = {"Nome":'Lethycia',"Ultimo nome": 'Ferreira',"Idade":'22',"Curso":'Programador de Sitemas',"Endereço":'Canada'}

print(pessoa)
print(pessoa['Nome'])
print(pessoa['Ultimo nome'])
print(pessoa['Idade'])
print(pessoa['Curso'])
print(pessoa['Endereço'])
del pessoa['Curso']
print(pessoa)
pessoa['Ultimo nome'] = 'Lopes'
print(pessoa)
pessoa['Curso'] = 'Programador de Sistemas'
print(pessoa)
print(pessoa['Endereço'])

pessoa2 = pessoa.copy()
pessoa2['Nome'] = 'Mayra'
pessoa2['Idade'] = '25'
print(pessoa2.items())