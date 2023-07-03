contador = 0
print('---SIMULADOR DE CAIXA ELETRÔNICO---')
cedulas = 0
while True:
    saque = 0
    valor = int(input('Qual o valor você deseja sacar?'))
    saque+=valor

    if valor>cedulas:
        print(valor/cedulas)