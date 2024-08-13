print('{:#^40}'.format(' PROGRESSÃO ARITIMÉTICA V.2 '))
print('GERADOR DE PA')
print('-='*10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')


