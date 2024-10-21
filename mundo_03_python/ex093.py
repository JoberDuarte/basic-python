aproveitamento = {}
aproveitamento['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {aproveitamento["Nome"]} jogou? '))
gols_marcados = []
for n in range(0,partidas):
    gol = int(input(f'Quantos gols na partida {n}? '))
    gols_marcados.append(gol)
aproveitamento['Gols'] = gols_marcados
aproveitamento['Total'] = sum(gols_marcados)
print('-='*30)
print(aproveitamento)
print('-='*30)
for k,v in aproveitamento.items():
    print(f'{k} = {v}')
print('-='*30)
print(f'O jogador {aproveitamento["Nome"]} jogou {partidas} partidas.')
for n in range(0,partidas):
    print(f'=> Na partida {n}, fez {aproveitamento["Gols"][n]}')