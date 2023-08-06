from random import sample
print('--------- PALPITES MEGA SENA ----------')
jogos = int(input('Quantos jogos você quer que eu sorteie ? '))
print(f'--------- SORTEANDO {jogos} JOGOS ----------')
palpites = list()
sub = list()
for c in range(1,jogos+1):
    sorteador = sample(range(0, 61), 6)
    sub.append(sorteador)
    palpites.append((sub[:]))
    sub.clear()
for p,v in enumerate(palpites):
    print(f'Jogo {p+1}: {v}')

