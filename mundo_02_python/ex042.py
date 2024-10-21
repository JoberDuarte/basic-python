a = int(input(' Tamanho da linha reta 1 = '))
b = int(input(' Tamanho da linha reta 2 = '))
c= int(input(' Tamanho da linha reta 3 = '))

if a<b+c and b<a+c and c<a+b:
    print('É possível formar um triângulo!')
    if a == b == c:
        print('É possível formar um triângulo equilátero')
    elif a == b and b != c or a == c and a != b or b == c and a != b:
         print('É possível formar um triângulo Isóceles')
    elif a != b and b != c and a != c:
         print('É possível formar um triângulo Escaleno')

else:
    print('Não é possivel formar um triângulo!')