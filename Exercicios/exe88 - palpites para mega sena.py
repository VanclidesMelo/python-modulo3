print('-' * 40)
print(f'{'JOGO NA MEGA SENA':^40}')
print('-' * 40)
from time import sleep
from random import randint
lista = []
jogos = []
quant = int(input('Quantos jogos você quer que eu sortei? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, f' < BOA SORTE! >', '-=' * 5)






