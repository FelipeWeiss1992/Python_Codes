pessoas = list()
dados = list()
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso :')))
    if len(pessoas) == 0:
      maiorpeso = menorpeso = dados[1]
    else:
      if dados[1] > maiorpeso:
        maiorpeso = dados[1]
      if dados[1] < menorpeso:
        menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar? [S/N] '))
    while r not in 'NnSs':
      r = str(input('Opção Invalida,Quer continuar? [S/N]'))
    if r in 'Nn':
      break
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso cadastrado foi {maiorpeso:.0f} KG. Peso de ',end= '')
for p in pessoas:
  if p[1] == maiorpeso:
    print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso cadastrado foi {menorpeso:.0f} KG. Peso de ',end= '')
for p in pessoas:
  if p[1] == menorpeso:
    print(f'[{p[0]}] ',end='')
