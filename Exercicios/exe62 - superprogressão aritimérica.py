print('{:#^40}'.format(' PROGRESSÃO ARITIMÉTICA V.2 '))
print('GERADOR DE PA')
print('-='*10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))



