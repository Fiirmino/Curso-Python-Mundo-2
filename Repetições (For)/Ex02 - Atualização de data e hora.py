from datetime import datetime
import time

for c in range (0,10):
    #time.sleep(5)
    hoje = datetime.now()
    hora_atual = hoje.strftime('%H:%M:%S')
    print(hora_atual)

