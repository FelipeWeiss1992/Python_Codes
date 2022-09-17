from datetime import date
atual = date.today().year
sexo = str(input('Sexo: M OU F ?'))
if sexo == 'F':
    print('Você não precisa se alistar')
    exit(0)
else:
    nasc = int(input('Ano de nascimento:'))
    idade = atual - nasc
if  idade == 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    print('Você tem que se alistar IMEDIATAMENTE!!!')
elif idade <= 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))












