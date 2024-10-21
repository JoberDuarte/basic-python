from random import randint
from time import sleep
from operator import itemgetter
jogador = {}
jogador['Jogador 1'] = randint(1,6)
jogador['Jogador 2'] = randint(1,6)
jogador['Jogador 3'] = randint(1,6)
jogador['Jogador 4'] = randint(1,6)

jogador_ordenado = dict(sorted(jogador.items(), key=itemgetter(1), reverse=True))
print('-='*15)
print(f"{'VALORES SORTEADOS':^10}")
print('-='*15)
for k, v in jogador.items():
    print(f'O {k} tirou {v} no DADO.')
    sleep(1)
print('-='*15)
print(f"{'RANKING DOS JOGADORES':^10}")
print('-='*15)
print(jogador_ordenado)

for i, (k , v) in enumerate(jogador_ordenado.items(), 1):
    print(f'{i}o lugar: {k} com {v}')
    sleep(1)