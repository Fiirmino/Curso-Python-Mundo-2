cont = 'a'
while cont !='N':
    num = int(input('Digite um número: '))
    multiplicacao = 1
    for c in range (num,0,-1):
        multiplicacao *=c
    print(f'A fatoração de !{num} é {multiplicacao}')
    cont = input('\nDeseja continuar o programa? [S/N] ...').upper()
