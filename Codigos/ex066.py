print('*' * 20)
print('CADASTRE UMA PESSOA')
print('*' * 20)
totmaior = homens = mulhermenor = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if idade >= 18:
            totmaior += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulhermenor += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totmaior}')
print(f'Ao todo temos {homens} homens cadastrados\nE temos {mulhermenor} mulheres com menos de 20 anos')





