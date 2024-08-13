print('{:*^40}'.format(' SOMA DOS PARES '))
cont = 0
soma = 0
for c in range (1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))








