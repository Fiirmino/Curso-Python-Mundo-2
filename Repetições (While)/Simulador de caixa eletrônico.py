contador = 0
print('---SIMULADOR DE CAIXA ELETRÔNICO---')
cedulas =
while True:
    saque = 0
    valor = int(input('Qual o valor você deseja sacar?'))
    saque+=valor

    if valor>cedulas:
        print(valor/cedulas)