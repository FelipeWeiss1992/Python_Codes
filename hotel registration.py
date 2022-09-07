print('-=' * 5, 'SUNRISE RESORT', '-=' * 5)
print('-=' * 4, 'CADASTRO DE HÓSPEDES', '-=' * 4)
qtde_hospedes = int(input('Quantos hóspedes?'))
quarto = []
for hospedes in range(qtde_hospedes):
    print(f'Hóspede {hospedes + 1}')
    nome = str(input('Nome: '))
    cpf = int(input('CPF: '))
    hospede = [nome, cpf]
    quarto.append(hospede)
for i in quarto:
    indice = quarto.index(i)
    print('Hóspedes Cadastrados')
    print(f'Nome: {quarto[indice][0]} Cpf: {quarto[indice][1]}')
