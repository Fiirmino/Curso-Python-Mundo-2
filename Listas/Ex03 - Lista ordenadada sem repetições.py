lista =[]

for c in range(1,6):
    lista.append(int(input(f'Digite o {c}° valor: ')))
lista.insert(0,min(lista))
lista.pop(5)
print(lista)