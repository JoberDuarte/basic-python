from random import randint
print('-='*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*10)
vitorias = 0
while True:
    num = int(input('Digite um número = '))
    escolha = str(input('Par ou Ímpar [P/I] = ')).strip().upper()
    pc = randint(0,5)
    total = num + pc
    print(f'Você escolheu {num} e o PC escolheu {pc}. Total de {total}', end=' ')
    print('DEU PAR'if total % 2 == 0 else 'DEU IMPAR')
    if total % 2 == 0:
        if escolha == 'P':
            vitorias += 1            
            print('Você venceu, vamos jogar novamente  ')
        else:
            break
    if total % 2 !=0:
        if escolha == 'I':
            vitorias += 1
            print('Você venceu, vamos jogar novamente  ')
        else:
            break
print(f'GAME OVER, você venceu {vitorias} vezes ')