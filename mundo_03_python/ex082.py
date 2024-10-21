num = []
pares = []
impares = []

while True:
     num.append(int(input('Digite um número = ')))
     continuar = str(input('Quer continuar? [S/N] ')).upper()
     if continuar != 'S':
          break

for c in num:
    if c % 2 == 0:
          pares.append(c)
    else:
         impares.append(c)
num.sort()
pares.sort()
impares.sort()
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')