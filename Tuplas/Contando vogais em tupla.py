nomes = ('biscoito','gabriel','jaca','acerola')
print('-=-=-='*10)
for nomes in nomes:
    Tem_vogais = ''
    for vogal in 'aeiou':
        if vogal in nomes:
            Tem_vogais += vogal
    Tem_vogais2 = '-'.join(Tem_vogais)
    print(f'{nomes} possui a(s) vogal(is): {Tem_vogais2}')
print('-=-=-='*10)
print('Fim do programa')

