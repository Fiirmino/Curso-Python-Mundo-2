lista = []
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num %2 == 0:
        par.append(num)
    else:
        impar.append(num)
    continuar = input('Deseja encerrar o programa ? [S/N]').strip().lower()[0]
    if continuar == 's':
        break
print('---'*20)
print(f'A lista completa é: {lista}')
print('---'*20)
print(f'Os números pares são: {par}')
print('---'*20)
print(f'Os números ímpares são: {impar}')
print('---'*20)
print('FIM DO PROGRAMA !!!')
print('---'*20)