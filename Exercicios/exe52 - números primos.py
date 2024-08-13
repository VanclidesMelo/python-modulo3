tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    print('{}'.format(c), end= ' ')
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end= '')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso ele É PRIMO')
else:
    print('Por isso ele NÃO É PRIMO')


