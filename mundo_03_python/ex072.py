numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número entre 0 e 20: '))
if n<0 or n> 20:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f' Você digitou o número {numeros[n]}')
