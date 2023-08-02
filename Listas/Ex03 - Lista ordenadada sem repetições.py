lista = []
for c in range (1,6):
    num = int(input(f'Digite o {c}° valor: '))
    lista.append(num)
    lista.sort()
    ultimo_elemento = lista[-1]
    if num == ultimo_elemento:
        print('Adicionado no final da lista')
    else:
        print(f'Adicionado na posição {lista.index(num)}')
print(lista)
print(ultimo_elemento)