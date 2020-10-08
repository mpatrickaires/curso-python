listaNumeros = list()

while True:
    listaNumeros.append(int(input('Digite um número: ')))

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

listaNumerosPar = list()
listaNumerosImpar = list()

for numeroAtual in listaNumeros:
    if numeroAtual % 2 == 0:
        listaNumerosPar.append(numeroAtual)
    else:
        listaNumerosImpar.append(numeroAtual)

print('-=' * 25)
print(f'A lista completa é {listaNumeros}')
print(f'A lista de pares é {listaNumerosPar}')
print(f'A lista de ímpares é {listaNumerosImpar}')
