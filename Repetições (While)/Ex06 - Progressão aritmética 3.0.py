#GERADOR DE P.A

num1 = int(input('Digite o primeiro termo da sua P.A: '))
num2 = int(input('Digite a razão desejada da P.A: '))
pa = num1
opcao = 10
total = 0
cont = 0

while opcao!=0:
    total +=opcao
    while cont<=total:
        cont+=1
        pa+=num2
        print(pa, end=' ')
    opcao = int(input('\nDeseja inserir mais quantos termos ?'))