
print('\033[4:30:47mSelecione uma das conversões abaixo:\033[m ')
print('(1) para binário')
print('(2) para octal')
print('(3) para hexadecimal')
conver = input('\033[4:30:47mNúmero da conversão:\033[m ')

if conver == '1':
    num = int(input('Digite um número para converter para binário: '))
    x = bin(num)
    print(x[2::])
elif conver == '2':
    num1 = int(input('Digite um número para converter para octal: '))
    x = oct(num1)
    print(x)
else:
    num2 = int(input('Digite um número para converter para Hexadecimal: '))
    x = hex(num2)
    print(x)