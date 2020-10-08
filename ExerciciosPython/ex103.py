def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if not gols.isnumeric():
        gols = '0'
    gols = int(gols)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


jogador = str(input('Nome do Jogador: ')).strip().title()
gol = str(input('Número de Gols: ')).strip()
ficha(jogador, gol)
