print('{:*^40}'.format(' MAIOR E MENOR DA SEQUÊNCIA '))
maior_peso = 0
menor_peso = 0
for pess in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pess)))
    if peso == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('O maior peso lido foi {}kg'.format(maior_peso))
print('O menor peso lido foi {}kg'.format(menor_peso))



