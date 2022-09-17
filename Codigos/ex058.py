from time import sleep
n1 = int(input('Primeiro Valor:'))
n2 = int(input('Segundo Valor:'))
opcao = 0
while opcao != 5:
    print('-=' * 12)
    print('''[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Numeros\n[5] Sair do Programa''')
    opcao = int(input('>>>>> Qual é a sua opção:'))
    if opcao == 1:
         print('A soma entre {} e {} é {}'.format(n1, n2, (n1 + n2)))
    elif opcao == 2:
      print('O resultado de {} x {} é {}'.format(n1, n2, (n1 * n2)))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
         print('Informe os números novamente:')
         n1 = int(input('Primeiro Valor:'))
         n2 = int(input('Segundo Valor:'))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção Invalida!!! Tente Novamente.')
print('-=' * 12)
print('Fim do Programa, Obrigado')