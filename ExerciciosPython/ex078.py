listaNumeros = list(int(input(f'Digite um valor para a posição {i}: ')) for i in range(0, 5))

print('=-' * 20)
print(f'Você digitou os valores {listaNumeros}')

print(f'O maior valor digitado foi {max(listaNumeros)} nas posições ', end='')
for posicao, valor in enumerate(listaNumeros):
    if valor == max(listaNumeros):
        print(f'{posicao}... ', end='')

print(f'\nO menor valor digitado foi {min(listaNumeros)} nas posições ', end='')
for posicao, valor in enumerate(listaNumeros):
    if valor == min(listaNumeros):
        print(f'{posicao}... ', end='')
