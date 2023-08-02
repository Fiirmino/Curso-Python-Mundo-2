galera = []
lista = []
tot = 0
print('---- CENTRAL DE CADASTRO -----')
while True:
    nome = input('Nome: ').strip()
    lista.append(nome)
    tot+=1
    peso = float(input('Peso: '))
    lista.append(peso)
    galera.append(lista[:])
    lista.clear()
    galera.sort()
    novo_usuario = input('Deseja cadastrar outra pessoa ? ').strip().lower()[0]
    if novo_usuario =='n':
        break
    for c in galera:
        maior_peso = max(galera)


print(galera)
print(f'Total de pessoas cadastradas: --> {tot} pessoas.')
