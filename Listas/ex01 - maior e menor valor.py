num =[]
for c in range (1,6):
    num.append(int(input(f'Digite o {c} número: ')))
print('-x-'*20)
print(num)
print(f'O maior número é {max(num)} e ele está na posição {num.index(max(num))}')
print(f'O menor número da lista é {min(num)} e ele está na posição {num.index(min(num))}')
print('-x-'*20)
