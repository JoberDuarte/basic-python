import random
n_usuario = int(input('Advinhe o número que o computador escolheu entre 1 a 5 = '))
n_computador = random.randint(1,5)
print('O número que o computador escolheu foi {}'.format(n_computador))

if n_usuario == n_computador:
    print('Você VENCEU!')
else:
    print('Você PERDEU!')
