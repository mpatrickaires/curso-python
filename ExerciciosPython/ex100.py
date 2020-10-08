from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')

    for sorteio in range(0, 5):
        numSorteado = randint(0, 10)
        lista.append(numSorteado)
        print(numSorteado, end=' ')
        sleep(0.5)

    print('PRONTO!')


def somaPar(lista):
    soma = 0

    for numeroAtual in lista:
        if numeroAtual % 2 == 0:
            soma += numeroAtual

    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
