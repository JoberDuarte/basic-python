palavras_aleatorias = (
    "Abacaxi", "Bicicleta", "Cachorro", "Dinossauro", "Elefante",
    "Foguete", "Girassol", "Hipopótamo", "Igreja", "Jabuticaba"
)

print(palavras_aleatorias)

for p in palavras_aleatorias:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra,end=' ')