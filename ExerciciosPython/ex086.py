listaMatriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        listaMatriz[linha].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))

print('-=' * 25)
for linha in listaMatriz:  # Anda por todas as listas dentro da listaMatriz
    for coluna in linha:  # Anda por todos os elementos dentro de cada lista em 'linha'
        print(f'[{coluna:^5}]', end='')
    print('')
