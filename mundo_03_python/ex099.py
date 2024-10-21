from time import sleep

def maior( * num):
    print('Analisando os valores passados...')
    lista = []
    for n in num:
        print(f'{n} ',end='', flush=True)        
        sleep(0.5)
        lista.append(n)
    if lista:
        print(f'Foram informados {len(lista)} valores ao todo.')
        print(f'O maior valor informado foi {max(lista)}')
        
    else:
        print('Nenhum valor foi informado')
    print('='*30)

maior(1,2,3,4,5)
maior(1,6,5,33,8,45,0)
maior()