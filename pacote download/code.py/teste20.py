#contagem regressiva de 10 a 0 com 1 segundo de espera
from time import sleep
for c in range (10,0,-1):
    sleep(1)
    print(c) 
    