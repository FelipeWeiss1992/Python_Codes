def area(larg, comp):
  a = larg * comp
  print(f'A área de um terreno {larg}x{comp} é de {a:.1f}m²')


#PROGRAMA PRINCIPAL
print('Controle de Terrenos')
print('-' * 20)
area(float(input('LARGURA (m): ')),float(input('COMPRIMENTO (m): ')))