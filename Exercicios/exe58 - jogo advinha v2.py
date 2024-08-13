print('{:=^40}'.format(' JOGO DO ADVINHA '))
from random import randint
print('''Sou seu computador...
Acabei de pensar em número de 0 a 10.
Será que você consegue advinhar qual foi? ''')
computador = randint(0,10)
acertou = False
cont = 0
while not acertou:
    palpite = int(input('Qual é seu palpite? '))
    cont += 1
    if palpite == computador:
        acertou = True
    else:
        if palpite < computador:
            print('Mais...Tente mais uma vez. ')
        elif palpite > computador:
            print('Menos...Tente mais uma vez. ')
print('Acertou com {} tentativas. Parabéns!'.format(cont))











