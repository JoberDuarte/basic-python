valor = int(input('Qual o valor da casa que deseja comprar? R$ = '))
salario = int(input('Qual o valor do seu salario atual? R$ = ')) 
tempo = int(input('Em quantos anos pretente financiar o imovel? = '))
max_prestacao = salario * 0.30
prestacao = valor/(tempo *12)

print('Valor máximo da prestação para aprovação = {:.2f}'.format(max_prestacao))
print('Valor da prestação mensal baseado no tempo = R${:.2f}'.format(prestacao))

if max_prestacao >= prestacao:
    print('PARABENS, o seu emprestimo foi APROVADO')
else:
    print('INFELISMENTE o  seu emprestimo foi REPROVADO')