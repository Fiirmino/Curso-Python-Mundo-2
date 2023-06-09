print('\033[1:4:30:47mALISTAMENTO MILITAR\033[m')
name = input('\033[1:31mInforme seu nome combatente: \033[m')
years = int(input('\033[1:31mQual a sua idade?\033[m '))

if years ==18:
    print('Hora de se alistar combatente !!')
elif years >18:
    falta = years-18
    print(f'\033[1:30:47mOlá {name} ainda faltam {falta} anos para seu alistamento\033[m')
else:
    falta = (years-18)*-1
    print(f'Olá {name} ainda faltam {falta} anos para você poder se alistar')