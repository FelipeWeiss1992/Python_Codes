while True:
    n = int(input('Quer ver a tabuada de qual valor:'))
    print('-=' * 7)
    if n < 0:
        break
    for c in range(1,11):
       print(f'{n} X {c} = {c * n}')
    print('-=' * 7)
print('PROGRAMA TABUADA ENCERRADO, Volte Sempre!')