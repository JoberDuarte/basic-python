from datetime import date
ano = int(input('Digite o seu ano de nascimento = '))
idade = date.today().year - ano

if idade <= 9:
    print('Sua categoria é  MIRIM')
elif idade > 9 and idade <= 14:
    print('Sua categoria é  INFANTIL')
elif idade >14 and idade <= 19:
    print('Sua categoria é  JUNIOR') 
elif idade >19 and idade <= 20:
    print('Sua categoria é  SÊNIOR')
else:
    print('Sua categoria é  MASTER')