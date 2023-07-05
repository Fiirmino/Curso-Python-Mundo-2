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
    rint(f'serão necessárias {qnt_ced} cédulas de R${ced}')
      break
    print('FIM DO PROGRAMA')