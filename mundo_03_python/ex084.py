lista_pessoas = []
dados = []
pessoas_obesas = []
pessoas_magras = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista_pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar a registrar? [S/N] '))
    if continuar in 'Nn':
        break

print(f'Ao todo você cadastrou {len(lista_pessoas)} pessoas')
print('As pessoas obesas com mais de 100kg são : ',end=' ')
for p in lista_pessoas:
    if p[1] >= 100:
        print(f'{p[0]}', end=' ')
print('\nAs pessoas magras com menos de 70Kg são: ',end=' ')
for p in lista_pessoas:
    if p[1] <= 70:
        print(p[0],end=' ')

