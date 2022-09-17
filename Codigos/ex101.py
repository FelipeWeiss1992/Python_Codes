def leiaInt(msg):
  ok = False
  valor = 0
  while True:
   n = str(input(msg))
   if n.isnumeric():
     valor = int(n)
     ok = True
   else:
     print('ERRO! Digite um número inteiro válido')
   if ok:
     break
  return valor



#Programa Principal
n = leiaInt('Digite um n:')
print(f'Voce acabou de digitar o número {n}')