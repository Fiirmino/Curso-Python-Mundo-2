num = int(input('Digite o primeiro termo: '))
num2 = int(input('Digite a razão: '))
termo = num
cont = 0
while cont<10:
    termo = termo+num2
    cont+=1
    print(f'{termo}', end=' ')