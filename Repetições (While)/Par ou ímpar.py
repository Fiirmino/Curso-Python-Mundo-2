from random import randint
contador = 0
while True:
    jogo2 = ''
    n = int(input('Digite um valor:'))
    par_impar = ''
    jogo = input('Você quer par ou ímpar ? [P/I]').strip()[0]
    jogo2+=jogo
    n2 = randint(0,10)
    soma = n+n2
    if soma%2 ==0:
        par_impar+='par'
    else:
        par_impar+= 'impar'
    print(f'Você jogou {n}, o computador jogou {n2}. A soma entre eles é {soma} deu {par_impar}')
    if jogo2 == par_impar[0]:
        print('Você ganhou, parabéns !!')
        contador+=1
    else:
        print(f'Voce perdeu, mas ganhou {contador} vezes')
        break
print('FIM DO PROGRAMA')