s = 0
for c in range (1,500):
    impar = c%2 == 1
    if impar == True:
        print(f'{c} ímpar')
        s+=c
print(f'A soma é: {s}')
