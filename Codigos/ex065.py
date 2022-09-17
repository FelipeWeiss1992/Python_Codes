from random import randint
print('-=-' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 10)
cont = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Diga um valor:'))
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print(' DEU PAR' if total % 2 == 0 else ' DEU IMPAR')
    if tipo == 'P':
        total = computador + jogador
        if total % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        total = computador + jogador
        if total % 2 != 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes')





