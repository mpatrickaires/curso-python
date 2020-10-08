tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio',
          'Athletico Paranaense', 'São Paulo', 'Internacional',
          'Corinthians', 'Fortaleza', 'Goiás', 'Bahia',
          'Vasco da Gama', 'Atlético', 'Fluminense', 'Botafogo',
          'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {tabela}')

print('-=' * 15)
print(f'Os 5 primeiros são {tabela[:5]}')

print('-=' * 15)
print(f'Os 4 últimos são {tabela[16:]}')

print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(tabela)}')

print('-=' * 15)
print(f'O Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição')
