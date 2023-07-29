exp = input('Digite uma expresão: ')
lista1 = []
lista2 = []
for c in exp:
    if '(' in c:
        lista1.append(c)
    elif ')' in c:
        lista2.append(c)
if len(lista1) == len(lista2):
    print('Expressão válida')
else:
    print('Expressão ínválida')
print('---'*20)
print('FIM DO PROGRAMA !!!')
print('---'*20)