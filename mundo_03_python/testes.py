def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        else:
            print('ERRO! Digite um número inteiro válido!')

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
