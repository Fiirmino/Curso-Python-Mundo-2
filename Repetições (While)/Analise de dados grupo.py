# CADASTRO DE PESSOAS
maior_18 = sexo_m = sexo_f_20 = 0
while True:
    print('---CADASTRE UMA PESSOA---')
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('sexo[M/F]: ').upper().strip()[0]
    if sexo =='M':
        sexo_m+=1
    if idade<20 and sexo =='F':
        sexo_f_20+=1
    if idade>=18:
        maior_18+=1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar [S/N]? ').upper().strip()[0]
    if continuar == 'N':
        break
print('----'*40)
print(f'O total de pessoas +18 anos é {maior_18}.')
print(f'Foram cadastrados {sexo_m} homens.')
print(f'Foram encontradas {sexo_f_20} mulheres com menos de 20 anos.')