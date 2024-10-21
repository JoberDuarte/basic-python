exp = str(input('Digite uma empressão = '))
lista = list(exp)
abrir = fechar  = 0
for c in lista:
    if c =='(':
        abrir += 1
    elif c ==')':
        fechar += 1
if abrir == fechar:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')