dados = []
pares = []
for c in range(1, 5):
    num = int(input(f'Digite o {c}° número: '))
    dados.append(num)
    if num%2 == 0:
        pares.append(num)
tupla = tuple(dados)
tupla2 = tuple(pares)
print(tupla)
print('--'*20)
if 9 in tupla:
    contador = tupla.count(9)
    print(f'O número 9 apareceu {contador} vezes')
else:
    print('Não foi encontrado valor 9')
print('--'*20)
if 3 in tupla:
    contador = tupla.index(3)
    print(f'O número 3 está na {contador+1}° posição')
else:
    print('Não foi detectado número 3')
print('--'*20)
print(f'Estes são os números pares {tupla2}')


