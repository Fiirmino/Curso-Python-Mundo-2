contador = soma = 0
continuar = 'a'
lista = []
while continuar!='N':
    n = int(input('Digite um número: '))
    lista.append(n)
    contador+=1
    soma+=n
    continuar = input('Quer continuar ?[S/N]').strip().upper()[0]
print('-'*50)
print(f'Você digitou {contador} números e a média entre eles é {soma/contador:.2f}')
print(f'O maior valor é {max(lista)} e o menor é {min(lista)}')
print('-'*50)
print('Fim do programa !!!')