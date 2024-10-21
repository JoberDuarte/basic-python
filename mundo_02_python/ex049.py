tabuada = int(input('Digite um número para saber a tabuada = '))
print('A Tabuada do {} é:'.format(tabuada))
print('-='*10)
for c in range(0,11):
    print('{} x {} = {}'.format(tabuada,c,c*tabuada))
print('-='*10)