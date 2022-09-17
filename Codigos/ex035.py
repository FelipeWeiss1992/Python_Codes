valor = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento:'))
prestacao = valor / (anos * 12)
minimo = (salario * 30 / 100)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de {:.2f}'.format(valor, anos, prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')



