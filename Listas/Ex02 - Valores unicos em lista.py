c = ''
lista =[]
while True:
    num = int(input('Digite um valor:'))
    if num in lista:
        print('O número informado ja está presente na lista, tente novamente...')
    else:
        lista.append(num)
        quer_continuar = input('Deseja inserir outro valor ? [S/N]').upper().strip()[0]
        if quer_continuar =='N':
            break
lista.sort()
print(lista)