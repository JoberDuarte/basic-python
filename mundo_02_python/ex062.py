termo = int(input('Digite o termo da PA = '))
razao = int(input('Digite a razão da PA = ')) 

s = 1
continuar = 10
total = 0
while continuar != 0:
    total = total + continuar
    while s <= total:
        n = termo + s*razao
        s +=1
        print(n,end=' -> ')
    print('Pausa')    

    continuar = int(input('Gostaria de ver mais quantos termos = '))
print('FIM, você analisou {} termos'.format(total))