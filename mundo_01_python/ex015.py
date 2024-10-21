kmr =float(input('Quantos km o carro rodou? '))
dias =int(input('Por quantos dias alugou o carro? '))
pkm =0.15*kmr
pd =60*dias
total=pkm+pd
print('O valor que terá de pagar é {:.2f}'.format(total))
