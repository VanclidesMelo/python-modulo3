print(f'{' LISTAS COM PARES E IMPARES ':*^40}')
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = (int(input(f'Digite o {c}º valor: ')))
    if valor % 2 == 0:
       num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 15)
num[0].sort()
num[1].sort()
print(f'Os valores pares são {num[0]}')
print(f'Os valores impares são {num[1]}')




