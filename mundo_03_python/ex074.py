import random
numeros = (random.choices(range(1,20), k=5))
#count = 0
#maior = 0
#menor = 0
print('Os valores sorteados foram: ',end='')
for n in numeros:
    print(n,end=' ')
   #count+=1
 #   if count == 1:
 #        maior = menor = n
 #   else:
 #       if n > maior:
 #           maior = n
 #       if n < menor:
 #           menor = n

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
    

