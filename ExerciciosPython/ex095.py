listaJogadores = list()
jogador = dict()
golPartidas = list()

while True:
    jogador['Nome'] = str(input('Nome do Jogador: ')).title().strip()

    qtdPartidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for partida in range(0, qtdPartidas):
        golPartidas.append(int(input(f'   Quantos gols na partida {partida + 1}? ')))

    jogador['Gols'] = golPartidas[:]
    jogador['Total'] = sum(golPartidas)

    listaJogadores.append(jogador.copy())
    golPartidas.clear()

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar in 'N':
        break

print('-=' * 30)
print(f'cod {"nome":<15}{"gols":<15}{"total":<15}')
print('-' * 50)
for numero, jogadorAtual in enumerate(listaJogadores):
    print(f'{numero:>3} {jogadorAtual["Nome"]:<15}{str(jogadorAtual["Gols"]):<15}{jogadorAtual["Total"]:<15}')

while True:
    print('-' * 50)
    numero = int(input('Mostrar dados de qual jogador? '))

    if numero == 999:
        print('<< VOLTE SEMPRE >>')
        break

    if numero >= len(listaJogadores):
        print(f'ERRO! Não existe jogador com código {numero}! Tente novamente.')

    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {listaJogadores[numero]["Nome"]}')
        for partida, gols in enumerate(listaJogadores[numero]['Gols']):
            print(f'   No jogo {partida + 1} fez {gols} gols.')
