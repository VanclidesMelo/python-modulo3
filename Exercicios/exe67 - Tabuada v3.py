print('{:#^40}'.format(' TABUADA V.3 '))
while True:
    v = int(input('Quer a tabuada de qual valor? '))
    print('-' * 40)
    if v < 0:
        break
    for c in range (1,11):
        print(f'{v} x {c} = {v*c}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO!')
