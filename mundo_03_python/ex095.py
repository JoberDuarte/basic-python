jogadores = []
aproveitamento = {}
gols_marcados = []
resposta = 's'
while resposta not in 'Nn':
    aproveitamento['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {aproveitamento["Nome"]} jogou? '))  
    for n in range(0,partidas):
        gol = int(input(f'Quantos gols na partida {n+1}? '))
        gols_marcados.append(gol)
    aproveitamento['Gols'] = gols_marcados[:]
    aproveitamento['Total'] = sum(gols_marcados)
    jogadores.append(aproveitamento.copy())
    aproveitamento.clear()
    gols_marcados.clear()
    resposta = str(input('Quer continuar [S/N]? '))
print('-='*30)
print(jogadores)
print('-='*30)
print('Cod.Nome             Gols         Total')
for k,v in enumerate(jogadores):
    print(f'{k:>3}  ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*30)

while True:
    busca = int(input('Mostrar detalhes de qual jogador [999 interrompe]? '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'Erro! Não Existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["Nome"]} --')
        for i, g in enumerate(jogadores[busca]["Gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')