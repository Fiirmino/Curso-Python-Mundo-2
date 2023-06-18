from datetime import datetime
import time

for c in range (0,10):
    #time.sleep(5)
    hoje = datetime.now()
    data_atual = hoje.strftime('%d/%m/%Y')
    hora_atual = hoje.strftime('%H:%M:%S')
    print('---------------------')
    print(f'data: {data_atual}')
    print(f'hora: {hora_atual}')
    print('---------------------')
    time.sleep(2)
print('FIM DO PROGRAMA')
