print('='*25)
print('CAIXA ELETRONICO')
print('='*25)
saque = int(input('Qual o valor que você quer sacar? R$:'))
while True:
    if saque != 0:
        notas50 = saque//50 
        resto1 = saque % 50
    if resto1 != 0:
        notas20 = resto1//20
        resto2 = resto1 % 20
    if resto2 != 0:
        notas10 = resto2//10
        resto3 = resto2 % 10
    if resto3!= 0:
        notas1 = resto3//1
        break                    
print(f'Total de {notas50} cédulas de R$50')
print(f'Total de {notas20} cédulas de R$20')
print(f'Total de {notas10} cédulas de R$10')
print(f'Total de {notas1} cédulas de R$1')
