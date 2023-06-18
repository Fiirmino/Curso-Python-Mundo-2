import time

num1 = int(input('Informe o primeiro termo da P.A: '))
num2 = int(input('Informe qual é a razão da P.A: '))
lista = [] #lista vazia que receberá valor futuramente
for c in range (num1,500,num2):
    lista.append(c) #Lista vazia receberá o valor de 'c'
    primeiros_termos = lista[:10]  #Informa os 10 primeiros termos da lista
print('Loading P.A...')
time.sleep(2)
print(f'De acordo com o primeiro termo informado e sua razão correspondente...\n P.A = {primeiros_termos}')
