from time import sleep
valor1 = int(input('Digite o 1º número inteiro = '))
valor2 = int(input('Digite o 2º número inteiro = '))
comando = 0
while comando != 5:
    print('-='*10)
    comando = int(input('''[1] Somar Valores
[2] Multiplicar Valores
[3] Mostrar Maior
[4] Novos números
[5] Sair do programa
                    
Escolha uma ação = '''))
    print('-='*10)

    if comando == 1:
        print('A soma dos valores é {}'.format(valor1+valor2))
    elif comando == 2:
        print('A multiplicação  dos valores é {}'.format(valor1*valor2))
    elif comando == 3:
        if valor1>valor2:
            print('O maior valor é {}'.format(valor1))
        elif valor1<valor2:
            print('O maior valor é {}'.format(valor2))
        else:
            print('Os valores são iguais')
    elif comando == 4:
        valor1 = int(input('Digite o 1º número inteiro = '))
        valor2 = int(input('Digite o 2º número inteiro = '))
    elif comando == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção invalida, tente novamente  ')
    

    
    
    
    
print('O Programa TERMINOU')