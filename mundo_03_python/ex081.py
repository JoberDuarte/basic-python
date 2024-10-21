num = []

while True:
     num.append(int(input('Digite um número = ')))
     continuar = str(input('Quer continuar? [S/N] ')).upper()
     if continuar != 'S':
          break
num.sort(reverse=True)
n = num.copy()
print(num)
print(f'Você digitou {len(num)} elementos')
print(f'Os valores em ordem descrescente são {n}') 
if 5 in num:
    print('O número 5 foi digitado na lista')
else:
    print('O número 5 NÃO foi digitado na lista')