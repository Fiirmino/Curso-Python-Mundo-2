from datetime import datetime
hoje = datetime.now()
media = []
maior_idade = 0
homem_mais_velho = ''
qnt_M_20 = 0
maior_idade_F = 0
mulher_mais_velha = ''

for c in range(1,6):
    print(f'----{c}° pessoa -----')
    nome = input('Informe seu nome: ').strip()
    idade = input('Informe sua data de nascimento: ')
    sexo = input('Qual seu sexo? [M/F])').strip()
    nascimento = datetime.strptime(idade,'%d/%m/%Y')
    if nascimento.month>hoje.month or nascimento.month==hoje.month and hoje.day>nascimento.day:
        idade = (hoje.year-nascimento.year-1)
    else:
        idade = (hoje.year-nascimento.year)
    media.append(idade)
    if sexo.upper() == 'M' and idade>maior_idade:
        maior_idade = idade
        homem_mais_velho = nome

    elif sexo.upper() == 'F' and idade>maior_idade_F:
            maior_idade_F = idade
            mulher_mais_velha = nome
    if sexo.upper() == 'F' and idade<20:
        qnt_M_20+=1

media_idade = sum(media)/len(media)
print(f'A média de idade das pessoas é de {media_idade:.0f} anos')
print(f'O homem mais velho possui {maior_idade} anos e seu nome é {homem_mais_velho}')
print(f'A quantidade de mulheres com menos de 20 anos é {qnt_M_20}')
print(f'A mulher mais velha possui {maior_idade_F} anos e seu nome é {mulher_mais_velha}')