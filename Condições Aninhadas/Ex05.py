import numpy
import numpy as np

nota1 = float(input('Insira a nota1: '))
nota2 = float(input('Insira a nota2: '))
media = (nota1+nota2)/2
if media<5:
    print('Reprovado')
elif media>=5 and media<=6.9:
    print('Recuperação')
else:
    print('Aprovado')