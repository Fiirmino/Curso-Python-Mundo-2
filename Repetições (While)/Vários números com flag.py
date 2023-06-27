contador = soma = 0
while True:
    n = int(input('Digite um valor: '))
    if n ==  999:
        break
    soma +=n
    contador += 1
print(f'foram digitados {contador} números e a soma entre eles é {soma}')