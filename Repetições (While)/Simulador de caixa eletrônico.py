
valor = int(input('Digite o valor de saque: R$'))
total = valor
ced = 50
qnt_ced = 0
while True:
    if total>=ced:
        total-=ced
        qnt_ced+=1
    else:
        if total>0:
            print(f'serão necessárias {qnt_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        qnt_ced=0
    if total == 0:
        print(f'serão necessárias {qnt_ced} cédulas de R${ced}')
        break
        print('FIM DO PROGRAMA')
valor = int(input('Digite quanto deseja sacar: R$'))
total = valor
real = 50
qnt_real = 0
while True:
    if valor <=0:
        print('Saque ínvalido !!!')
        break
    if total>=real:
        total-=real
        qnt_real+=1
    else:
        if qnt_real>0:
            print(f'Entregue {qnt_real} notas de R${real}')
        if total ==0:
            break
        if real ==50:
            real = 20
        elif real == 20:
            real = 10
        elif real == 10:
            real = 1
        qnt_real = 0
print('FIM DO PROGRAMA')
