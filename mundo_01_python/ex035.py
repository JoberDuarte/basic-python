a = int(input(' Tamanho da linha reta 1 = '))
b = int(input(' Tamanho da linha reta 2 = '))
c= int(input(' Tamanho da linha reta 3 = '))

if a<b+c and b<a+c and c<a+b:
    print('É possível formar um triângulo!')
else:
    print('Não é possivel formar um triângulo!')