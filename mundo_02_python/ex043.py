peso = float(input('Qual o seu peso?  Kg= '))
altura = float(input('Qual a sua altura? metros = '))

imc = peso/(altura**2)
print('Seu imc é = {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está acima do peso!') 
elif imc >= 30 and imc < 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida!')