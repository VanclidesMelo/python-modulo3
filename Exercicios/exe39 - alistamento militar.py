from datetime import date
ano = int(input('Ano da nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade > 18:
    alistamento = idade - 18
    ano_alistamento = atual - alistamento
    print('Você já deveria ter se alistado há {} anos.'.format(alistamento))
    print('Seu alistamento foi em {}.'.format(ano_alistamento))
elif idade < 18:
    alistamento = 18 - idade
    ano_alistamento = atual + alistamento
    print('Ainda faltam {} anos para o alistamento.'.format(alistamento))
    print('Seu alistamento será em {}.'.format(ano_alistamento))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!.')



