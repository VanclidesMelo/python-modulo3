print(('{:=^30}').format(' CONTAGEM REGRESSIVA '))
from time import sleep
for c in range (10, -1, -1):
    print(c)
    sleep(0.5)
print('BUM! BUM! POOW')
