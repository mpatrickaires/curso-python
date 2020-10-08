listaMatriz = [[], [], []]
somaPares = somaTerceiraColuna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        listaMatriz[linha].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))

print('-=' * 25)
for linha in listaMatriz:  # Anda por todas as listas dentro da listaMatriz
    somaTerceiraColuna += linha[2]  # Soma o valor do terceiro elemento da lista atual em 'linha'

    for coluna in linha:  # Anda por todos os elementos dentro de cada lista em 'linha'
        print(f'[{coluna:^5}]', end='')

        if coluna % 2 == 0:  # Verifica se o elemento atual em 'coluna' é par
            somaPares += coluna
    print('')
print('-=' * 25)

print(f'A soma dos valores pares é {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}.')
print(f'O maior valor da segunda linha é {max(listaMatriz[1])}.')

