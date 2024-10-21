preco = float(input('Qual o valor do produto = R$'))
pagamento = int(input('''Forma de pagamento digite:
[1] Dinheiro/Cheque (desconto de 10% avista)
[2] Cartão (desconto de 5% avista)
Digite aqui sua escolha = '''))
if pagamento == 1:
    print('O valor a pagar será de R${:.2f}'.format(preco*0.9))  
elif pagamento == 2:  
    parcela = int(input('''Em quantas parcelas:
[1] A vista (5% de desconto)
[2] 2x no cartão (preço normal)
[3] 3x ou mais no cartão (20% de juros)
Digite aqui sua escolha ='''))
    if parcela == 1:
        print('O valor a pagar será de R${:.2f}'.format(preco*0.95)) 
    elif parcela == 2:
        print('O valor a pagar será de R${:.2f}'.format(preco)) 
    elif parcela == 3:
        np= (int(input('Em quantas vezes vai pagar? = ')))
        print('Você vai pagar R${:.2f}, dividido em {} vezes e cada parcela vai dar R${:.2f}'.format(preco*1.2, np,(preco*1.2)/np ))

    

        '''print('O valor a pagar será de R${:.2f}'.format(preco*1.2))'''
        
    else:
        print('Valor INVALIDO começe o processo novamente')
else:
    print('Valor INVALIDO começe o processo novamente')

