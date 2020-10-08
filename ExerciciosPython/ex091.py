from random import randint
from time import sleep
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}

print('Valores sorteados: ')
for key, value in jogadores.items():
    print(f'   O {key} tirou {value}')
    sleep(1)

print('Ranking dos jogadores: ')
jogadoresOrdem = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
for numero, jogador in enumerate(jogadoresOrdem):
    print(f'   {numero + 1}º lugar: {jogador[0]} com {jogador[1]}')
    sleep(1)
