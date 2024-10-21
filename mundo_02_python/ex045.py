import random 
from time import sleep
 
print('-='*10)  
participante = str(input('Escolha entre Pedra, Papel ou Tesoura = ')).strip()
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POOO!!!')
opcoes = ['PEDRA','PAPEL','TESOURA']
pc = random.choice(opcoes)
part = (participante.upper())
print('-='*15)
print('Computador escolheu {}'.format(pc))


if part == 'PEDRA' or part == 'PAPEL' or part == 'TESOURA':
    print('Você escolheu {}'.format(part))
else:
    print('{} = Você digitou errado tente novamente'.format(participante))
print('-='*15)    

if part == pc:
    print('EMPATE')
elif part == 'PEDRA' and pc == 'PAPEL':
    print('VOCÊ PERDEU')
elif part == 'PEDRA' and pc == 'TESOURA':
    print('VOCÊ GANHOU')
elif part == 'PAPEL' and pc == 'PEDRA':
    print('VOCÊ GANHOU')
elif part == 'PAPEL' and pc == 'TESOURA':
    print('VOCÊ PERDEU')
elif part == 'TESOURA' and pc == 'PAPEL':
    print('VOCÊ GANHOU')
elif part == 'TESOURA' and pc == 'PEDRA':
    print('VOCÊ PERDEU')
