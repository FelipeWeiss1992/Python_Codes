print('=' * 14)
print('BAZAR XINGLING')
print('=' * 14)
valor = float(input('Valor das compras: R$ '))
print('''FORMAS DE PAGAMENTO')
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    parc = valor / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parc))
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    parc = int(input('Quantas parcelas? '))
    vezes = total / parc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parc, vezes))
else:
    total = valor
    print('OPÇÃO INVALIDA de pagamento. Tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))