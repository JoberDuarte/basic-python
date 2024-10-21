lista = []
pessoa = {}
resposta = 's'
soma = media = 0
while resposta not in 'Nn':
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro, por favor digite apenas M ou F')
    pessoa['Idade'] =int(input('Idade: '))
    soma += pessoa['Idade']
    lista.append(pessoa.copy())
    pessoa.clear()
    resposta = str(input('Quer continuar [S/N]? '))
print(lista)
print('-='*30)
print(f'=> O grupo tem {len(lista)} pessoas')
media = soma / len(lista)
print(f'=> A média de idade é de {media} anos')
print('=> As mulheres cadastradas foram ', end='')
for pessoa in lista:
    if pessoa['Sexo'] == 'F':
        print(pessoa['Nome'],end='')
print()
print('=> Lista das pessoas que estão acima da média:')
for pessoa in lista:
    if pessoa['Idade'] > media:
        print('   ')
        for k, v in pessoa.items():
            print(f'{k} = {v}  ',end='')
        print()