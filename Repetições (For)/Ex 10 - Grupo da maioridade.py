from datetime import datetime
hoje = datetime.now()
tot = 0
for c in range(1,8):
    idade = input('Informe sua data de nascimento: ')
    nascimento = datetime.strptime(idade,'%d/%m/%Y')
    maioridade = hoje.year-nascimento.year
    if maioridade>=18:
        tot +=1
        print('De maior')
        if hoje.month < nascimento.month or hoje.month == nascimento.month and hoje.day < nascimento.day:
            maioridade = (hoje.year - nascimento.year) - 1
            print(f'Você possui {maioridade} anos, logo não é de maior')
    else:
        print(f'Você possui {maioridade} anos, logo não é de maior')
print(f'o total de pessoas de maior são ')




