print('{:*^40}'.format(' TUPLAS COM TIMES DE FUTEBOL '))
times = ('Atletico-PR', 'Bahia', 'Flamengo', 'Botafogo', 'Cruzeiro', 'Atletico Mineiro', 'Bragantino', 'Palmeiras',
         'São Paulo', 'Internacional', 'Fortaleza', 'Grêmio', 'Vasco', 'Criciuma', 'Juventude', 'Corinthians',
         'Fluminense', 'Vitoria', 'Atletico-GO', 'Cuiabá')
print('-=' * 30)
print(f'Lista dos Times do Brasileirão 2024: {times}')
print('-=' * 30)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 30)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'O São Paulo está na {times.index('São Paulo')+1}ª posição')
