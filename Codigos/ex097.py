from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores da lista :', end=' ')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!!!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}')


def somaimpar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 1:
            soma += valor
    print(f'Somando os valores impares de {numeros}, temos {soma}')


def somatotal(lista):
    total = sum(numeros)
    print(f'Somando todos os valores de {numeros}, temos {total}')


#PROGRAMA PRINCIPAL
numeros = list()
sorteia(numeros)
somapar(numeros)
somaimpar(numeros)
somatotal(numeros)