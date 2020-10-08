cont = 0
soma = 0
for c in range(1, 501, 2):  # Laço de repetição se repete de 0 até 500 e saltando 2 pois assim só realiza ímpares
    if c % 3 == 0:  # Verifica se o número 'c' é DIVÍSIVEL POR 3
        soma = soma + c
        cont = cont + 1
print(f'A soma de todos os {cont} números ímpares que são múltiplos de 3 entre 1 e 500 é {soma}')
