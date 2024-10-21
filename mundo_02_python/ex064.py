quantidade = soma = 0

n = int(input('Digite um número [999 para encerrar] = '))
while n != 999:    
    quantidade += 1
    soma += n
    n = int(input('Digite um número [999 para encerrar] = '))
print(f'Você digitou {quantidade} números e a soma entre eles é {soma}')