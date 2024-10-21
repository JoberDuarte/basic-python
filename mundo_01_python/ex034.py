salario = int(input('Qual é o seu salário atual ? = R$'))
if salario > 1250:
    print('PARABÉNS, você receberá um aumento de 10% e passará a ganhar {:.2f}'.format(salario*1.10))
else:
    print('PARABÉNS, você receberá um aumento de 15% e passará a ganhar {:.2f}'.format(salario*1.15))