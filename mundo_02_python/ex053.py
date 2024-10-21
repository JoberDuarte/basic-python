frase = str(input('Digite uma frase = ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Essa frase é um PALINDROMO')
else:
    print('Essa frase não é um PALINDROMO')









# frase = str(input('Digite uma frase = ')).strip().replace(' ','').upper()
# frase_inv = frase[::-1]
# print('O inverso de {} é {}'.format(frase, frase_inv))
# if frase == frase_inv:
#     print('Essa frase é um PALINDROMO')
# else:
#    print('Essa frase não é um PALINDROMO')