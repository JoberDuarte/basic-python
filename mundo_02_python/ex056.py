soma_idade = 0
maior_idade = 0
mulher_idade = 0
velho = 0
for c in range(1,5):    
    nome = str(input('Digite o nome da {}ª pessoa = '.format(c)))
    idade = int(input('Digite a idade da {}ª pessoa = '.format(c)))
    sexo = int(input('''Digite o sexo da {}ª pessoa:
    [1] Masculino
    [2] Feminino
    Resposta ='''.format(c)))
    soma_idade += idade
    if sexo ==1:
        if idade > maior_idade:
            maior_idade = idade 
            if maior_idade == idade:
               velho = nome
    if sexo == 2:
        if idade <  20:
            mulher_idade += 1  
print('A média de idade deste grupo de peessoas é {}'.format(soma_idade/4))
print('O nome do homem mais velho é {} e ele tem {}'.format(velho, maior_idade))
print('{} é a quantidade de mulheres com menos de 20 anos'.format(mulher_idade))



