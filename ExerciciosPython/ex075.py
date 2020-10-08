tuplaNumeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
                int(input('Digite outro número: ')), int(input('Digite o último número: ')))

print(f'Você digitou os valores {tuplaNumeros}')

print(f'O valor 9 apareceu {tuplaNumeros.count(9)} vezes')

if 3 in tuplaNumeros:
    print(f'O valor 3 apareceu na {tuplaNumeros.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram ', end='')
for posicao in tuplaNumeros:
    if posicao % 2 == 0:
        print(posicao, end=' ')
