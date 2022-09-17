n = int(input('Digite um numero para saber sua tabuada:'))
print('-=' * 6)
print('Tabuada de {}'.format(n))
print('-=' * 6)
for aux in range(1,11):
    print('{} X {} = {}'.format(n, aux, (n * aux)))