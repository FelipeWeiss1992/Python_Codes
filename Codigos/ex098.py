from datetime import date

def voto(ano):
  anoatual = date.today().year
  idade = anoatual - ano
  if idade < 16:
      return f'Com {idade} anos: NÃO VOTA.'
  elif 16 <= idade < 18 or idade > 65:
      return f'Com {idade} anos: VOTO OPCIONAL.'
  else:
      return f'Com {idade} anos: VOTO OBRIGATORIO.'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

