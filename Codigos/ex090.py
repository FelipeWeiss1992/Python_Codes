dados = dict()
partidas = list()
dados['nome'] = str(input('Nome do Jogador? '))
tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, tot):
  partidas.append(int(input(f'Quantos gols na partida {c} ? ')))
  dados['gols'] = partidas[:]
  dados['total'] = sum(partidas)
print('-=' * 20)
print(dados)
print('-=' * 20)
for k, v in dados.items():
  print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {dados["nome"]} jogou {tot} partidas')
for i, v in enumerate(dados['gols']):
 print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')