print('-'*50)
n =  int(input('Deseja inserir quantos termos da sequencia de fibonacci: '))
print('-'*50)
#0-1-1-2-3-5-8
t1 = 0
t2 = 1
contador = 0
t3 = 0
print(f'{t1}-->{t2}', end= '')
while contador<=n-3:
    t3 = t1+t2
    t1 = t2
    t2 = t3
    contador+=1
    print(f'-->{t3}', end='')
print('\nMuito obrigado por usar meu programa !!')
print('-'*50)