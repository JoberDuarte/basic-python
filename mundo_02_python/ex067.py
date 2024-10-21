while True:
    tabuada = int(input('Qual número você quer saber a tabuada? = '))
    print(f'A tabuada de {tabuada} é :')
    print('-='*10)
    for c in range (1,11):
        print(f'{tabuada} x {c} = {tabuada*c}')
    print('-='*10)
    if tabuada < 0:
        break
print('FIM do programa')


