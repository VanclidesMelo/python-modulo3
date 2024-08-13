print('{:=^40}'.format(' MENU DE OPÇÕES '))
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
    opcao = int(input('>>> Qual é sua opção? '))
    if opcao == 1:
        somar = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, somar))
    elif opcao == 2:
        resultado = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, resultado))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        else:
            print('Os dois valores são iguais')
    elif opcao == 4:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente!')
    print('-='*10)
print('Fim do programa. Volte sempre!')
