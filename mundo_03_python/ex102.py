def fatorial(num, show = False):
    ''' --> Calcula o fatorial de um número
    Para '''
    f = 1 
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ',end='')
        f *= c
    return f 





#Programa Principal
print(fatorial(5, show = True))
help(fatorial)