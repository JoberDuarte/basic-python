matriz = [[0,0,0], [0,0,0], [0,0,0]]
pares = []
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
   
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()  # Para mover para a próxima linha após imprimir os elementos da linha atual

print(f'A soma dos valores pares é {sum(pares)}')
print(f'A soma dos valores da terceira coluna é {(matriz[0][2] + matriz[1][2] + matriz[2][2])}')
print(f'O maior valor da segunda coluna é {max(matriz[1])}')
