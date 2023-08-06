turma = list()
sub = list()
while True:
    sub.append(input('Nome: '))
    n1 = float(input('Nota1: '))
    n2 = float(input('Nota2: '))
    sub.append(n1)
    sub.append(n2)
    media = sub.append((n1+n2)/2)
    turma.append(sub[:])
    sub.clear()
    parada = input('Quer continuar ? [S/N]: ').strip().lower()[0]
    if parada == 'n':
        break
print('---'*15)
print('No --  NOME  --  MÉDIA')
print('---'*15)
for p, dados in enumerate(turma):
    print(f'{p} -- {dados[0]} -- {dados[-1]}')
print('---'*15)
maior_nota = 0
for maior in turma:

ind = int(input('Mostrar notas de qual aluno ? (999 encerra): '))
if ind == 999:
    exit()
print(f'As notas de {turma[ind][0]} são Nota1: ({turma[ind][1]}) e Nota2: ({turma[ind][2]})')
