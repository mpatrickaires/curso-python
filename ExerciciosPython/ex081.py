listaValores = list()

while True:
    valor = int(input('Digite um valor: '))
    listaValores.append(valor)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Você digitou {len(listaValores)} elementos.')

listaValores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {listaValores}')

print('O valor 5 faz parte da lista!' if 5 in listaValores else 'O valor 5 não foi encontrado na lista!')
