nome = str(input('Escreva seu nome completo = ')).strip()
n = nome.split()
n2 = n[::-1]
print('Primeiro nome é {}'.format(n[0]))
print('Último nome é {}'.format(n2[0]))