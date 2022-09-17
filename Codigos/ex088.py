ficha = list()
while True:
  nome = str(input('Nome:'))
  nota1 = float(input('Nota 1:'))
  nota2 = float(input('Nota 2:'))
  media = (nota1 + nota2) / 2
  ficha.append([nome, [nota1, nota2], media])
  resp = str(input('Quer continuar: [S/N] '))
  if resp in 'Nn':
    break
print('-=' * 20)
print(f'{"N°":<4}{"NOME":>10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
  print(f'{i:<4}{a[0]:>10}{a[2]:>8.1f}')
print('-' * 25)
while True:
  opc = int(input('Mostrar notas de qual aluno? [N°] (999 Finaliza)'))
  if opc <= len(ficha) - 1:
    print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
  elif opc == 999:
    break
  print('-' * 35)
print('FINALIZANDO...')
print('OBRIGADO!')

