print('\033[1:33:40mSIMULADOR DE EMPRÉSTIMO BANCÁRIO\033[m')

casa = int(input('Insira o valor da casa desejada: R$'))
anos = int(input('Em quantos anos deseja pagar ? '))
salario = float(input('Qual sua renda mensal? R$'))


prestacao = casa/(anos*12)
print(f'Para quitar um imóvel de R${casa} em {anos}anos a prestação ficaria em R${prestacao:.2f}')
if prestacao <= salario*0.3:
    print('Empréstimo aprovado !!')
else:
    print('Empréstimo negado pela política de credito!')