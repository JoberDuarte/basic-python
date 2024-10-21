nota_1 = float(input('Qual foi a sua nota da P1 = '))
nota_2 = float(input('Qual foi a sua nota da P2 = '))

media = (nota_1 + nota_2)/2
print('A sua média foi {:.1f}'.format(media))

if media < 5:
    print('Você foi REPROVADO')
elif 5 <= media or media >= 6.9:
    print('Voce está de RECUPERAÇÃO')
else:
    print('Parabéns, você foi APROVADO')