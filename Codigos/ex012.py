salário = float(input('Qual o salario do funcionario? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento\n'
      'passa a receber R${:.2f}'.format(salário, novo))