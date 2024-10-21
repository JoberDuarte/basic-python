from datetime import date
pessoa = {}
pessoa['Nome'] = str(input('NOME: '))
ano = int(input('ANO DE NASCIMENTO: '))
pessoa['Idade'] = date.today().year - ano
pessoa['CTPS'] = int(input('CARTEIRA DE TRABALHO (0 caso não tenha): '))
if pessoa['CTPS'] != 0:
    pessoa['CONTRATAÇÃO'] = int(input('ANO DE CONTRATAÇÃO: '))
    pessoa['SALÁRIO'] = float(input('SALÁRIO: '))
    pessoa['APOSENTADORIA'] = ((pessoa['CONTRATAÇÃO'] + 35) - date.today().year) + pessoa['Idade']
for k, v in pessoa.items():
    print(f'{k} = {v}')

