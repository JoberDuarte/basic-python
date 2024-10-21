print('='*25)
print('CADASTRE UMA PESSOA')
print('='*25)
maiores = homens = mulheres = 0
while True:    
    idade = int(input('IDADE = '))
    sexo  = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F] = ')).strip().upper()[0]
    continuar =' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] = ')).strip().upper()[0]
    print('--'*20)
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens+=1
    if sexo == 'F':
        if idade < 20:
            mulheres += 1
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos foi  = {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'Temos {mulheres} mulheres com menos de 20 anos')