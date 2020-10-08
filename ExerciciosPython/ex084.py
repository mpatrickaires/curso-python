listaGalera = list()
listaPessoa = list()
listaPesos = list()

while True:
    listaPessoa.append(str(input('Nome: ')).strip().title())
    listaPessoa.append(float(input('Peso: ')))

    listaPesos.append(listaPessoa[1])  # Adiciona o peso na lista de pesos
    listaGalera.append(listaPessoa[:])  # Adiciona o nome e o peso na lista completa de pessoas
    listaPessoa.clear()  # Limpa todos os dados da lista de pessoa para não acumular listas

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(listaGalera)} pessoas.')

print(f'O maior peso foi de {max(listaPesos)}Kg. Peso de ', end='')
#  Anda por todas as listas de pessoas na lista total:
for pessoa in listaGalera:
    if pessoa[1] == max(listaPesos):  # Verifica se o peso da pessoa atual é igual ao maior peso da lista de pesos
        print(f'[{pessoa[0]}] ', end='')  # Caso seja igual, printa o nome da pessoa

print(f'\nO menor peso foi de {min(listaPesos)}Kg. Peso de ', end='')
#  Mesmo esquema do for de cima, só que dessa vez com o menor peso da lista de pesos
for pessoa in listaGalera:
    if pessoa[1] == min(listaPesos):
        print(f'[{pessoa[0]}] ', end='')
