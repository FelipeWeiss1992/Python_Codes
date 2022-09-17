valores = list()
while True:
    n = (int(input('Digite um valor:')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
        valores.sort()
    else:
        print('Você ja adicionou esse valor')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Voce digitou os valores {valores}')
