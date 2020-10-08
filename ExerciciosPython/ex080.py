listaValores = list()

for cont in range(0, 5):

    valor = int(input('Digite um valor: '))
    if cont == 0 or valor > max(listaValores):
        listaValores.append(valor)
        print('Adicionado ao final da lista...')

    else:
        for posicao in range(0, len(listaValores)):
            if valor <= listaValores[posicao]:
                listaValores.insert(posicao, valor)
                print(f'Adicionado na posição {posicao} da lista...')
                break

print('-=' * 20)
print(f'Os valores digitados em ordem foram {listaValores}')
