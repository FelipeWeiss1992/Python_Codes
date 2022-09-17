valores = list()
npar = list()
nimpar = list()
while True:
    n = int(input('Digite um valor:'))
    valores.append(n)
    if n % 2 == 0:
        npar.append(n)
    else:
        nimpar.append(n)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    while r not in 'SN':
        r = str(input('Opção Inválida, Quer continuar? [S/N] ')).strip().upper()
    if r in 'N':
        break
print(f'Os valores digitados foram {valores}')
print(f'Os valores Pares digitados foram {npar}')
print(f'Os valores Impares digitados foram {nimpar}')