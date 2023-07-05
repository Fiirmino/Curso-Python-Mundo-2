#TUPLAS SÃO IMUTÁVEIS
import time

extenso = ('zero', 'um', 'dois','três','Quatro','Cinco', 'seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')

while True:
    num = int(input('Qual número você deseja escrever por extenso ? [0-20]: '))
    print(f'{num} por extenso é {extenso[num]}')
    time.sleep(1)
    continuar = input('Deseja escrever outro número ?[S/N]').upper().strip()[0]
    if continuar == 'N':
        break
print('Obrigado por usar o programa')