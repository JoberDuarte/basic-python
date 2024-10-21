termo = int(input('Digite o termo da PA = '))
razao = int(input('Digite a razão da PA = ')) 

s = 1
while s <= 10:
    n = termo + s*razao
    s +=1
    print(n,end=' -> ')
print('FIM')
