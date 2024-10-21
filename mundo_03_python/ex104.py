def leiaint(msg):
   ok = False
   while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
            ok = True
        else:
            print('ERRO! Digite um número inteiro valido!')
        if ok:
            break
        

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o {n} número.')
            
