#PAGAMENTO DE PRODUTO

preco_produto = float(input('Informe o preço do produto: R$'))
forma_pagamento = input('\033[1:4mQual a forma de pagamento?\033[m \n1- À vista(dinheiro/cheque)\n2- À vista cartão\n3- Cartão parcelado\n--> ')

if forma_pagamento=='1':
    print('Você tem direito a 10% de desconto')
    print(f'Valor final R${preco_produto-preco_produto*0.10:.2f}')
elif forma_pagamento=='2':
    print('Você tem direito a 5% de desconto')
    print(f'valor final R${preco_produto-preco_produto*0.05:.2f}')

if forma_pagamento =='3':
    parcelas = int(input('Informe o valor das parcelas:'))
    if parcelas ==2:
        print(f'Preço normal R${preco_produto:.2f}')
    else:
        print(f'juros de 20% --> R${preco_produto+preco_produto*0.20:.2f}')


