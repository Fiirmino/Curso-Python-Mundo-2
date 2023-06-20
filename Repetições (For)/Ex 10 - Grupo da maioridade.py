from datetime import datetime
hoje = datetime.now()
for c in range(1,8):
    idade = input('Informe sua data de nascimento:')
    nascimento = datetime.strptime(idade,'%d/%m/%Y')
    maioridade = hoje-nascimento
    if maioridade>=18:
        print('maior')
    elif nascimento.month>=hoje.month and nascimento.year<hoje.year:
        print('Você não é de maior')
    else:
        print('Você não é de maior')


