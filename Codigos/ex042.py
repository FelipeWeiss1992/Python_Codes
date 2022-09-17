peso = float(input('Qual seu peso? (KG) '))
altura = float(input('Qual sua altura? (M) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO')
elif 30 <= imc < 40:
    print('ATENÇÃO!!! Você está com OBESIDADE')
elif imc >= 40:
    print('CUIDADO!!! Você está com OBESIDADE MORBIDA')