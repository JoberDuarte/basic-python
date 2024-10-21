n1 = int(input('Digite o primeiro valor = '))
n2 = int(input('Digite o segundo valor = '))
n3 = int(input('Digite o terceiro valor = '))
n4= int(input('Digite o quarto valor = '))
valores = (n1,n2,n3,n4)

print(f'Voce digitou os valores {valores}')
print(f'O Valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O Valor 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não está entre os números escolhidos')
print('Os valores pares digitados foram ', end='')
for n in valores:
    if n % 2 == 0:
        print(n,end=' ')
      