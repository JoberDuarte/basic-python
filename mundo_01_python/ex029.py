import random
v = random.randint(60,180)

if v > 80:
    print('Você ultrapassou a velocidade maxima de 80km/h em {}km/h'.format(v-80))
    print('Isso gerou uma multa de R${},00. O que corresponde a R$7.00 por km acima do limite.'.format((v-80)*7))