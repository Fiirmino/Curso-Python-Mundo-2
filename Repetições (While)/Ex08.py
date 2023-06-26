contador = num = soma = 0
#num = 0
#soma = 0
num = int(input('Digite um número: (Caso queira parar digite 999): '))
while num!=999:
    contador+=1
    soma+=num
    num = int(input('Digite um número: (Caso queira parar digite 999): '))
print(f'Foram digitados {contador} numeros a soma entre eles é {soma}')