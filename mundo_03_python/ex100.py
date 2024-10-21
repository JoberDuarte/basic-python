from random import randint
from time import sleep
lista = []
def sorteio(list):
    print('='*50)
    print('Sorteando 5 valores da lista: ',end='')
    for n in range(0,5):
        a = randint(0,99)
        print(f'{a} ', end='', flush=True)
        sleep(0.3)      
        lista.append(a)
    print('PRONTO!')
    print('='*50)

def somapar():
    par = 0
    for i in lista:
        if i % 2 == 0:
            par += i
    print(f'Somando os valores pares de {lista}, temos {par}')

    


sorteio(lista)
somapar()