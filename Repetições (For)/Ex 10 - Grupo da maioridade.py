from datetime import datetime
hoje = datetime.now()
tot = 0
for c in range(1,8):
    idade = input('Informe sua data de nascimento: ')
    nascimento = datetime.strptime(idade,'%d/%m/%Y')
    if 
        maioridade = (hoje.year-nascimento.year)-1
    else:
        maioridade = (hoje.year-nascimento.year)
    if maioridade >=18:
        tot+=1
        print(f'Você é de maior,pois possui {maioridade} anos !')
    else:
        print(f'Você é de menor, pois possui {maioridade} anos!')
