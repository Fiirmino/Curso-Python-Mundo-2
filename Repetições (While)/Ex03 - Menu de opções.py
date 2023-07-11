import time
c = 0
maior = []
while c<5:
    for i in range (1,3):
        num =int(input(f'Digite o {i}° número:'))
        maior.append(num)
    print('[1]SOMA')

    print('[2]MULTIPLICAÇÃO')
    print('[3]MAIOR NÚMERO')
    print('[4]NOVOS NÚMEROS')
    print('[5]ENCERRAR O PROGRAMA')
    c = int(input('Escolha uma opção: num}'))
    if c == 1:
        print(f'A soma de {num} é {sum(maior)}')
        maior.clear()
    elif c == 2:
        print(f'A multplicação entre {num}x{num} = {num*num}')
        maior.clear()
    elif c == 3:
        print(f'O maior número entre {maior} é {max(maior)}')
        maior.clear()
    elif c ==4:
        time.sleep(1)
        print('Insira novos números...')
        maior.clear()
print('FIM DO PROGRAMA')