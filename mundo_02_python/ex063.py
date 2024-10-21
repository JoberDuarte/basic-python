print('---'*10)
print('SEQUENCIA DE FIBONNACI')
print('---'*10)
n  = int(input('Quantos elementos da sequência de FIBONACCI você quer verificar? = '))

total = 0
fib1 = 0
fib2 = 1
while total < n:
    fib = fib1+fib2
    fib1 = fib2
    fib2 = fib
    total+=1
    print('0 --> 1 -->',fib,end=' --> ')
print('FIM')