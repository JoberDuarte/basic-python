from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('='*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    cont = i  
   
    if i < f:  
        while cont <= f:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont+=p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont-=p
        print('FIM')


#Programa Principal
contador(1,10,1)
contador(10,0,2)
print('='*30)
print('Agora é sua vez de personalizar a contagem')
ini = int(input('Inicio: '))
fin = int(input('Final: '))
pas = int(input('Passo: '))
contador(ini, fin, pas)

