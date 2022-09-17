cont = ('zero','um', 'dois ','três','quatro','cinco','seis',
        'sete','oito','nove','dez','onze','doze','treze','catorze',
        'quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
opcao = ' '
while True:
    num = int(input('Digite um numero entre 0 e 20:'))
    if 0 <= num <= 20:
        print(f'Você digitou o numero {cont[num]}')
        opcao = str(input('Quer continuar? [S/N]')).strip().upper()
        if opcao != 'S':
            opcao = str(input('Quer continuar? [S/N]')).strip().upper()
            if opcao == 'N':
                break
print('OBRIGADO!!!')