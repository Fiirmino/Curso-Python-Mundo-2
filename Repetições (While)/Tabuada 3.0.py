import time

while True:
    contador = 0
    mult = 0
    n = int(input('Qual número vc quer ver a tabuada? '))
    if n <0:
        print('Número não suportado')
        time.sleep(1)
        print('Encerrando o programa')
        break
    while contador<10:
        contador+=1
        mult = n*contador
        if contador >0 and contador<=10:
            print(f'{n}x{contador} = {mult}')


