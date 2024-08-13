print(f'{' CONTANDO VOGAIS EM TUPLA ':*^40}')
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p.lower():
        if letra in 'aeiou':
            print(letra, end=' ')


      
      

