soma = 0
total = 0
maior = menor  = 0
continuar = 'S'
while continuar not in 'N':
    n = int(input('Digite um valor = '))
    soma += n
    total += 1
    if total == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Você quer continuar [S/N] = ')).strip().upper()[0]
print(f'A média entre os valores digitados foi {soma/total}, o maior valor foi {maior} e o menor valor foi {menor}.')