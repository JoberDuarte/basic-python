from datetime import date
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Qual o ano de nascimento da {}ª pessoa? = '.format(c)))
    idade = date.today().year - ano 
    if idade >= 21:
       maior += 1
    else:
        menor += 1
print('O número de pessoas maiores de idade é {}'.format(maior))
print('O número de pessoas menores de idade é {}'.format(menor))
       
