contador = total_compra = preco_1000 = menor_preco = 0
nome_menor = ''
print('------- LOJÃO ------')
while True:
    nome = input('Nome do produto: ').strip()
    preco = float(input('Preço do produto: R$'))
    total_compra += preco
    contador+=1
    if contador ==1:
        nome_menor = nome
        menor_preco = preco
    if preco<=menor_preco:
        nome_menor=nome
        menor_preco=preco
    if preco>=1000:
        preco_1000+=1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar [S/N]? ').strip().upper()[0]
    if continuar == 'N':
        break
print('----'*40)
print(f'O total da compra foi de R${total_compra:.2f}')
print(f'Foram encontrados {preco_1000} produtos maior que R$1000')
print(f'O item de menor valor é {nome_menor} e ele custou R${menor_preco:.2f}')