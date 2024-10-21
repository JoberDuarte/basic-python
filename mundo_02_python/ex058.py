import random
pc = random.randint(0,10)
tentativas = 0
jogador = int(input('Tente adivinhar o número que o PC pensou = '))
while jogador != pc:    
    if jogador < pc:
        jogador = int(input('MAIS... tente novamente = '))
        tentativas+=1
    if jogador > pc:
        jogador = int(input('MENOS... tente novamente = '))
        tentativas+=1
print('Você Acertou e precisou apenas de {} tentativas'.format(tentativas))