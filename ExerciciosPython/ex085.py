listaTotal = [[], []]

for cont in range(1, 8):
    valor = int(input(f'Digite o {cont}º valor: '))
    if valor % 2 == 0:
        listaTotal[0].append(valor)
    else:
        listaTotal[1].append(valor)

listaTotal[0].sort()
listaTotal[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {listaTotal[0]}')
print(f'Os valores ímpares digitados foram: {listaTotal[1]}')
