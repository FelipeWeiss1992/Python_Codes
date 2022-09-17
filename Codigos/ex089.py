from datetime import datetime
trabalhadores = dict()
trabalhadores['nome'] = str(input('Nome:'))
nasc = int(input('Ano de Nascimento:'))
trabalhadores['idade'] = datetime.now().year - nasc
trabalhadores['ctps'] = int(input('Carteira de Trabalho (0 não tem):'))
if trabalhadores['ctps'] != 0:
    trabalhadores['anocontr'] = int(input('Ano de Contratação:'))
    trabalhadores['salario'] = int(input('Salário: R$'))
    trabalhadores['aposentadoria'] = trabalhadores['idade'] + ((trabalhadores['anocontr'] + 35) - datetime.now().year)
print('-=' * 15)
for k, v in trabalhadores.items():
  print(f' - {k} tem o valor {v}')
