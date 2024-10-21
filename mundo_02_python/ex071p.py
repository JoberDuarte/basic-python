print('='*25)
print('CAIXA ELETRONICO')
print('='*25)
saque = int(input('Qual o valor que você quer sacar? R$:'))
total  = saque
ced = 50
totced = 0
while True:
    if total >=ced:
        total -= ced
        totced += 1
    else:
        print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced =20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break