preco = float(input('Qual é o preço do produto? R$ '))
desc = 5*preco/100
vf = preco-desc
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco,vf))
