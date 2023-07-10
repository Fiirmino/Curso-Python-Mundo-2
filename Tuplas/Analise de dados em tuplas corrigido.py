tupla = (
         int(input('Digite um número: ')),
         int(input('Digite o 2° número: ')),
         int(input('Digite o 3° número: ')),
         int(input('Digite o 4° número: '))
         )
print(f'Os números presentes na tupla são {sorted(tupla)}')
print(f'O número 9 apareceu {tupla.count(9)}')
if 3 in tupla:
    print(f'Número 3 está na {tupla.index(3)+1}° posição')
else:
    print('Não foi encontrado o número 3')
for c in tupla:
    if c%2 == 0:
        print(f'O número {c} é par')