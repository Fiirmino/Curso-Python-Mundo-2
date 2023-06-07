print('\033[1:33:40mSIMULADOR DE EMPRÉSTIMO BANCÁRIO\033[m')

casa = int(input('Insira o valor da casa desejada: R$'))
anos = int(input('Em quantos anos deseja pagar ? '))
salario = float(input('Qual sua renda mensal? R$'))
prestacao = casa/(anos*12)

if prestacao <= salario*0.3:
    print('\033[1:30:47mEmpréstimo aprovado !!\033[m')
    print(
        f'\033[1:30:47mPara quitar um imóvel de R${casa} em {anos} anos a prestação ficaria em R${prestacao:.2f}\033[m')
else:
    print('\033[1:30:47mEmpréstimo negado pela política de credito!\033[m')