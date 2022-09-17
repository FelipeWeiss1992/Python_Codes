times = ('America-MG','Atletico-PR','Atletico-Go','Atletico-MG','Avai','Botafogo',
        'Ceara','Corinthians','Coritiba','Cuiaba','Flamengo','Fluminense','Fortaleza',
        'Goias','Internacional','Juventude','Palmeiras','Bragantino','Santos','Sao paulo')
print('-=' * 15)
print(f'Lista de times do Brasileirão 2022: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Avai está na {times.index("Avai")+1}ª posição')