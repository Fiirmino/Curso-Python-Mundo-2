import random
'''num_aleatorio = 0
for c in range (1,6):
    sorteio = random.randint(0,10)'''
num_aleatorio = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10),random.randint(0,10))
print('---'*20)
print(num_aleatorio)
print('---'*20)
print(f'O maior valor é {max(num_aleatorio)}')
print(f'O menor valor é {min(num_aleatorio)}')
print('---'*20)
print('FIM DO PROGRAMA')