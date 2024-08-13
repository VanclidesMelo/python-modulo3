print('{:*^30}'.format(' NÚMERO POR EXTENSO '))
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {extenso[num]}')
    continuar = ' '
    if continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().split()[0]
        if continuar == 'N':
            break
print('FIM DO PROGRAMA!')


