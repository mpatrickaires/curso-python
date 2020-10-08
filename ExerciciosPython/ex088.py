from random import randint
from time import sleep

listaJogos = list()
listaSorteio = list()

print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)

qtdJogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{f" SORTEANDO {qtdJogos} JOGOS ":=^40}')

for jogo in range(0, qtdJogos):
    print(f'Jogo {jogo + 1}: ', end='')

    for sorteio in range(0, 6):
        numero = randint(1, 60)
        while numero in listaSorteio:
            numero = randint(1, 60)
        listaSorteio.append(numero)

    listaSorteio.sort()
    listaJogos.append(listaSorteio[:])
    print(listaJogos[jogo])
    sleep(1)
    listaSorteio.clear()

print(f'{" BOA SORTE! ":=^40}')
