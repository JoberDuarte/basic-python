nome = str(input('Qual seu nome? '))
if nome == 'Jober':
    print('Que nome diferente')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print(' Seu nome é popular no Brasil')
else:
    print('Seu nome é normal')
print('Tenha um bom dia {}'.format(nome))