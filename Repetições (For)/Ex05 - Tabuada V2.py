num = int(input('Informe um número para ver sua respectiva tabuada: '))
print('--------------------')
for c in range (1,11):
    mult = num*c

    print(f'{num}x{c} = {mult}')
print('--------------------')