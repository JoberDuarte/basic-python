s = str(input('Qual o seu sexo?[M/F] = ')).upper().strip()[0]
while s not in 'MF':  
    s= str(input(' Digite o sexo corretamente?[M/F] = ')).upper().strip()[0]
print('Sexo {} registrado com suceso'.format(s))