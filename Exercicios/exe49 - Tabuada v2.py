print('{:=^40}'.format(' TABUADA V2 '))
num = int(input('Digite um número para ver sua tabuada: '))
for c in range (1, 11):
    print('{} x {} = {}'.format(num, c, c*num))

