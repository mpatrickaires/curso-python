jogador = dict()
golPartidas = list()

jogador['Nome'] = str(input('Nome do Jogador: ')).title().strip()

qtdPartidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for partida in range(0, qtdPartidas):
    golPartidas.append(int(input(f'   Quantos gols na partida {partida}? ')))

jogador['Gols'] = golPartidas[:]
jogador['Total'] = sum(golPartidas)
print('-=' * 30)
print(jogador)

print('-=' * 30)
for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}.')

print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for partida, gols in enumerate(jogador['Gols']):
    print(f'    => Na partida {partida}, fez {gols} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
