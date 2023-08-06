matriz = list()
sub = list()
soma_pares = 0
for c in range(0,3):
    for v in range(0,3):
        sub.append(int(input(f'Digite [{c},{v}] da matriz: ')))
    matriz.append(sub[:])
    sub.clear()
for geral in matriz:
    for conjunto in geral:
        print(f'[ {conjunto} ]',end=' ')
        if conjunto%2 == 0:
            soma_pares+=conjunto
    print('')
print('---'*15)
print(f'A soma de todos os números pares da matriz é {soma_pares}')
print('---'*15)
print(f'O maior valor da segunda coluna é: {max(matriz[1])}')
print('---'*15)
print(f'A soma dos valores da terceira coluna é: {matriz[0][2]+matriz[1][2]+matriz[2][2]}')