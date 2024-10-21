soma = 0
for c in range(1,501,2):
  if c % 3 == 0:
    soma += c
print(' A soma dos números multiplos de 3 de 0 a 500 é {}'.format(soma))