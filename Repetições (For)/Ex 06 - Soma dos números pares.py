
lista_pares = []
for c in range(0, 6):
    num = int(input('Informe um número inteiro: '))
    par = num%2 == 0

    if par:
        lista_pares.append(num)
        soma = sum(lista_pares)
print(f'Estes são os números pares -->{lista_pares}')
print(f'A soma total de todos os números pares é {soma}')






