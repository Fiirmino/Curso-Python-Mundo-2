total = 1
dados = list()
sub = list()
mais_pesados = list()
while True:
    print(f'--- {total}° pessoa ---')
    sub.append(input('Nome: '))
    sub.append(int(input('idade: ')))
    sub.append(float(input('Peso: ')))
    dados.append(sub[:])
    sub.clear()
    total+=1
    print('----'*15)
    parada = input('Deseja encerrar o programa ? ').strip().lower()[0]
    if parada == 's':
        break
    for geral in dados:
        for sublista in geral:

            mais_pesados.append(geral)


print('---'*15)
print(f'Foram cadastradas {total-1} pessoas')
print('---'*15)

