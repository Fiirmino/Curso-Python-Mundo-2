import random
num = 0
tot = 0
sort = random.randint(0,10)
while num != sort:
    print(sort)
    num = int(input('Digite um número inteiro:'))
    if num != sort:
        tot+=1
print(f'Parabéns você acertou depois de {tot} tentativas')