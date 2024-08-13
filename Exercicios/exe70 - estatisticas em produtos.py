print('{:*^40}'.format(' PROGRAMA ESTATISTICAS EM PRODUTOS '))
print('-' * 30)
print('{:^30}'.format('LOJAS O BARATÃO'))
print('-' * 30)
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

'''
    simplificando o codigo e eliminando o else, ficaria assim:
     if cont == 1 or preco < menor
        menor = preco
        barato = produto
'''





