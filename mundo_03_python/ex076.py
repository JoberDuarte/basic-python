produtos_escolares = ("Lápis", 1.50,"Caneta", 2.25,"Caderno", 5.99,"Borracha", 0.99,"Régua", 1.75,
"Estojo", 3.49,"Tesoura", 2.99,"Cola", 1.99,"Papel sulfite (pacote)", 4.50,"Mochila", 20.99)
print('-='*20)
print(f'{'LISTAGEM DE PRECOS':^40}')
print('-='*20)
for pos in range(0, len(produtos_escolares)):
    if pos % 2 ==0:
        print(f'{produtos_escolares[pos]:.<30}',end='')
    else:
        print(f'R${produtos_escolares[pos]:>6.2f}')

