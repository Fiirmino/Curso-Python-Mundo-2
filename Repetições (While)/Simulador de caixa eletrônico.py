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