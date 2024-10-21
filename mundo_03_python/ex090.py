alunos = {}
alunos['Nome'] = str(input('Nome: '))
alunos['Média'] = float(input('Média: '))
for k, v in alunos.items():
    print(f'{k} é igual a {v}')

if alunos['Média'] >= 7:
    print('Situação: APROVADO')
elif 5 <= alunos['Média'] < 7:
    print('Situação: RECUPERAÇÃO')
else:
    print('Situação: REPROVADO')