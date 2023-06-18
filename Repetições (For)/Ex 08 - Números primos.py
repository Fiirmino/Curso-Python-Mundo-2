num = int (input('Digite um número inteiro: '))
qnt_primos = 0
lista = []
for c in range (1,num+1):
    primos = num%c == 0
    if primos:
        qnt_primos = qnt_primos+1
        lista.append(c)
    else:
        n_primos = lista
if qnt_primos == 2:
    print(f'\n{num} é um número primo. Pois ele é divisível por \033[33m{lista}\033[m')
else:
    print(f'{num} não é um número primo. Pois ele é divisível por \033[33m{n_primos}\033[m')















