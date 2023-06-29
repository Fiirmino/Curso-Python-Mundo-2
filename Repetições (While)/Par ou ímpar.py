from random import randint
contador = 0
while True:
    n = int(input('Digite um valor:'))
    par_impar = ''
    jogo = input('Você quer par ou ímpar ? [P/I]').strip()[0]
    n2 = randint(0,10)
    soma = n+n2
    if soma%2 ==0:
        par_impar+='par'
    else:
        par_impar+= 'ímpar'
    print(f'Você jogou {n}, o computador jogou {n2}. A soma entre eles é {soma} deu {par_impar}')

