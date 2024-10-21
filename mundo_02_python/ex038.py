print('Vamos fazer a comparação entre números')

n1 = int(input('Digite o primeiro número = '))
n2 = int(input('Digite o segundo número = '))

if n1 > n2:
    print('{} é maior que {}'.format(n1,n2))
elif n1 < n2:
    print('{} é maior que {}'.format(n2,n1))
else:
    print('Não existe valor maior, os dois são iguais')