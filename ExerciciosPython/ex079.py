listaValores = list()

while True:

    valor = int(input('Digite um valor: '))
    if valor not in listaValores:
        listaValores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('-=' * 30)
listaValores.sort()
print(f'Você digitou os valores {listaValores}')
