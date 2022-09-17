tabela = ('Lápis', 1.50,'Borracha', 2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,
        'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
print('-='* 20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-='* 20)
for pos in range(0,len(tabela)):
    if pos % 2 == 0:
        print(f'{tabela[pos]:.<30}',end=' ')
    else:
        print(f'R${tabela[pos]:.2f}')
print('-='* 20)