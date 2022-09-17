from random import randint
computador = randint(0,10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10
Será que voce consegue adivinhar qual foi?''')
jogador = (int(input('Qual é seu palpite? ')))
tentativas = 1
while jogador != computador:
     if jogador > computador:
        print('Menos... Tente mais uma vez.')
        jogador = int(input('Qual é seu palpite? '))
        tentativas += 1
     elif jogador < computador:
         print('Mais... Tente mais uma vez.')
         jogador = int(input('Qual é seu palpite? '))
         tentativas += 1
print('Acertou!!! Com {} tentativas. Parabéns'.format(tentativas))