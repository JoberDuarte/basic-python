lista = []
nomes = []
notas = []
n ='s'
while n not in "Nn":
    nome = str(input('Digite o nome do Aluno = '))
    nomes.append(nome)
    nota_1 = float(input('Qual foi a 1ª nota = '))
    notas.append(nota_1)
    nota_2 = float(input('Qual foi a 2ª nota = '))
    notas.append(nota_2)
    nomes.append(notas[:])
    lista.append(nomes[:])
    notas.clear()
    nomes.clear()
    n = str(input('Quer continuar? [S/N]'))
print('No.    Nome     Média')
print('--'*15)
for i,l in enumerate(lista):
    print(f'{i} {l[0]:^15} {sum(l[1])/2}')
print('--'*15)
aluno = 0
while True:
    aluno = int(input('Mostrar notas de qual aluno? [999 interrompe] = '))
    if aluno != 999:        
        print(f'As notas da {lista[aluno][0]} são {lista[aluno][1]}') 
        print('--'*15)
    else:
        break
print('FIM DA ANALISE')