from datetime import date
menor = 0
maior = 0
for c in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))




