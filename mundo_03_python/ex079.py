num = []
c = 'S'
while c not in 'Nn':
    n = int(input('Digite um valor: '))
    if n in num:
        print('Valor Duplicado! Não vou adicionar')
    else:
        num.append(n)
        print('Valor adicionado com sucesso...')
    c = str(input('Quer continuar? [S/N] '))
print(f'Você digitou os valores {sorted(num)}')