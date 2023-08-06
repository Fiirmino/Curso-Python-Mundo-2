lista = list()
par = list()
impar = list()
for c in range(1,8):
    num = int(input(f'Digite o {c}° número: '))
    if num%2 == 0:
        par.append(num)
        lista.sort()
    else:
        impar.append(num)
        lista.sort()
lista.append(par)
lista.append(impar)

print(f'Os números pares são {lista[0]}')
print('---'*15)
print(f'OS Números ímpares são {lista[1]}')