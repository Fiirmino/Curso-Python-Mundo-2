num = (
         int(input('Digite um número: ')),
         int(input('Digite o 2° número: ')),
         int(input('Digite o 3° número: ')),
         int(input('Digite o 4° número: '))
         )
print(f'Os números presentes na tupla são {sorted(tupla)}')
print(f'O número 9 apareceu {tupla.count(9)}')
print(f'O número 3 está na {tupla.index(3)}° posição')
for c in num :
    if tupla%2 == 0:
        print(f'O número {tupla} é par')