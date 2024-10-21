num = []

for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > num[len(num)-1]:
        num.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print('-='*20)
print(f'Os valores digitados em ordem foram {num}')



