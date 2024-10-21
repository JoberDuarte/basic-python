def ficha():
    jogador = str(input('Nome do Jogador: ')).strip()
    gols = str(input('Número de gols: ')).strip()
    if jogador == '':
        jogador = '<descobhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


ficha()