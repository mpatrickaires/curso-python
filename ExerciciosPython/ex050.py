soma = 0
cont = 0
for c in range(1, 7):  # Executa o laço de repetição 6 vezes, pois ao chegar em 7 o laço não é executado
    numero = int(input(f'Digite o {c}º número --> '))  # Pede o número da posição de 'c'
    if numero % 2 == 0:  # Verifica se o número digitado é PAR
        soma = soma + numero
        cont = cont + 1
print(f'QTD DE NÚMEROS PARES DIGITADOS --> {cont} \nSOMA DOS NÚMEROS PARES DIGITADOS --> {soma}')

