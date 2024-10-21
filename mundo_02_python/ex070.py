print('='*25)
print('LOJINHA DO PYTHON')
print('='*25)

total = 0
mais_1k = 0
mais_barato = 0
nome = 0
count = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco  = float(input('Preço : R$ '))
    continuar = str(input('Quer continuar? [S/N] = ')).strip().upper()[0]
    
    total += preco
    count+=1
    if count == 1:
        mais_barato = preco
        nome = produto
    else:
        if preco < mais_barato:
            mais_barato = preco
            nome = produto
    if preco > 1000:
        mais_1k += 1
    if continuar == 'N':
        break
print(f'O total da compra foi de R${total}')
print(f'O número de produtos mais caros que R$1000,00 foi  = {mais_1k}')
print(f'O produto mais barato foi {nome} e custou R$ {mais_barato}')