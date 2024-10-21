valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
print(f'Você digitou os valores {valores}')
print(f'O Maior valor digitado foi {max(valores)} nas posições ', end='')
for i, v in enumerate(valores):
   if v == max(valores):
       print(f'{i}...',end='') 
   

print(f'\nO Menor valor digitado foi {min(valores)} nas posições ',end='')
for i, v in enumerate(valores):
   if v == min(valores):
       print(f'{i}...',end='') 