num = int(input('Escolha um número inteiro qualquer = '))
escolha = int(input('''Digite o numero correspontende para converter em:
[1] BINÁRIO 
[2] OCTAL  
[3] HEXAGONAL  
                    
Escreva sua escolha aqui = '''))
if escolha == 1:
    print('{} em binário é = {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} em octal é = {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} em hexagonal é = {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')