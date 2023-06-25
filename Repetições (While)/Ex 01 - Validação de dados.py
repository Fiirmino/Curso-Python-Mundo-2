sexo = ' '
while sexo !='M' and sexo !='F':
    sexo = input('Informe seu sexo [M/F]:').upper()
    if sexo !='M' and sexo!='F':
        print('\033[1:31mInforme um sexo válido\033[m')
print('\033[1:32mValidação concluída!!\033[m')