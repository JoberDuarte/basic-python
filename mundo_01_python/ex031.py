km = int(input('Qual a distância da sua viagem? = '))
if km <= 200:
    print('O custo da viagem será de R${}'.format(km*0.50))
else:
    print('O custo da viagem será de R${}'.format(km*0.45))