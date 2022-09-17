pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] '))
    while pessoa['sexo'] not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] '))
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    resp = str(input('Quer continuar? [S/N] '))
    while resp not in 'SsNn':
        print('ERRO! Responda apensa S ou N.')
        resp = str(input('Quer continuar? [S/N] '))
    galera.append(pessoa.copy())
    if resp in 'Nn':
        break
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:.2f}')
print(f'C) As mulheres cadastradas foram ', end= '')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
