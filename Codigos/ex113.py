def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero inteiro válido')
            continue
        except (KeyboardInterrupt):
            print('\nUsuario não digitou nenhum valor')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um numero real válido.')
            continue
        except (KeyboardInterrupt):
            print('\nUsuario não digitou nenhum valor')
            return 0
        else:
            return n

n1 = leiaInt('Digite um valor inteiro:')
n2 = leiaFloat('Digite um valor real:')
print(f'O valor inteiro digitado foi {n1} e o valor real foi {n2}')