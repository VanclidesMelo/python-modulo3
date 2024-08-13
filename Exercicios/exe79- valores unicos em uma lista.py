print(f'{' VALORES UNICOS EM UMA LISTA ':*^40}')
valores = list()
continuar = ''
while True:
    num = (int(input('Digite um valor: ')))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
