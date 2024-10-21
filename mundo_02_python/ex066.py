soma =  n_digitados = 0
while True:           
    numero = (int(input('Digite um número [Digite 999 para encerrar] = ')))
    if numero == 999:
        break
    soma += numero
    n_digitados += 1
print(f'O programa leu {n_digitados} números e a soma entre eles é {soma}')