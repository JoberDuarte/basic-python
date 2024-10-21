#Manipulando texto - Fatiamento 
frase = str('  Curso em Vídeo Python  ')
#FATIAMENTO
#nesse caso ele vai do 9 ate o 21, pulando de 3 em 3
print(frase[9:21:3])
#nesse caso começa no cacartere 0 e vai ate onde voce escolher depois dos :
print(frase[:5])
# nesse caso ele começa onde indicou o inicio e vai ate o final 
print(frase[15:])
#nesse caso vai do 9 ate o final, pulando de 3 em 3
print(frase[9::3])
#ANALISE
#len = comprimento
print(len(frase))
#mostra a quantidade de letras na string
print(frase.count('o'))
# mostra a quantidade de letras na string, com fatiamento
print(frase.count('o',0,13))
#mostra onde ele encontra esse termo, ele mostra número do inicio do termo
print(frase.find('deo'))
# ele retorna -1 quando não encontra o termo
print(frase.find('android'))
# isso é um operador in, que mostra verdadeiro ou falso
print('curso' in frase)

# TRANSFORMAÇÂO
#troca palavras dentro da string
print(frase.replace('Python','Android'))
#Ele passa todas maiuscula
print(frase.upper())
#Esse faz o contrario do upper
print(frase.lower())
# Esse abaixo ele coloca tudo para minusculo, e a primeira letra ele deixa em maiuscula
print(frase.capitalize())
#Esse ele coloca em maicuscula cada primeira letra de cada palavra
print(frase.title())
# Essa função tira os estamos do inicio e final da string
print(frase.strip())
# Essa função "r" na frente do strip, significa que é do lado direito, para o outro lado é "l"
print(frase.rstrip())

#DIVISÃO
print(frase.split())

#JUNÇÃO
print('-'.join(frase))