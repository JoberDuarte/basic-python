numero = int(input('Digite um número para saber o fatorial = '))

t = numero - 1
fatorial = numero
while t > 1 :
    fatorial *= t
    t -= 1
print('O fatorial de {} é {}'.format(numero,fatorial))