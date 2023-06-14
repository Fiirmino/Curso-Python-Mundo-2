#IDADE DOS ATLETAS

idade = int(input('insira a idade do atleta: '))
if idade<=9:
    print('Categoria: Mirim')
elif idade>9 and idade<=14:
     print('Categoria: infantil')
elif idade>14 and idade<=19:
    print('junior')
elif idade>19 and idade<=20:
    print('Sênior')
else:
    print('Master')