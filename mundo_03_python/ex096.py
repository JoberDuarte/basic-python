def area():
    print('CONTROLE DE TERRENO')
    print('--'*10)
def area2(l,c):
    print(f'A area de um terreno é {l}x{c} é de {l*c}m²')

# Programa Principal
area()
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area2(l,c)