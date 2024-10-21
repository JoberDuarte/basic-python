from datetime import datetime

def calcular_idade(data_nascimento):
    hoje = datetime.now()
    nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) <(nascimento.month, nascimento.day))
    return idade

data_nascimento = input('Digite a data de seu nascimento (AAAA-MM-DD) = ')

try:
    idade = calcular_idade(data_nascimento)
    print('A sua idade atual é: {} anos'.format(idade))
except ValueError:
    print('Formato de idade invalido; Digite o formato corretamente AAAA-MM-DD')

if idade > 18:
    print('O seu tempo de alistamento já passou faz {} anos'.format(idade-18))
elif idade < 18:
    print('Ainda faltam {} anos para você se alistar'.format(18-idade))
else:
    print('Você tem 18 anos ou está prestes a fazer, este é o momento de se alistar!')