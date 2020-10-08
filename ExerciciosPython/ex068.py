from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
vitorias = 0

while True:
    computador = randint(0, 10)

    usuario = int(input('Diga um valor: '))
    while usuario < 0:
        usuario = int(input('Diga um valor: '))

    opcao = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    while opcao != 'P' and opcao != 'I':
        opcao = str(input('Par ou Ímpar? [P/I] ')).upper().strip()

    total = computador + usuario
    print('-' * 30)

    print(f'Você jogou {usuario} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 30)

    if (total % 2 == 0 and opcao == 'I') or (total % 2 == 1 and opcao == 'P'):
        print('Você PERDEU!')
        print('-=' * 15)
        break

    print('VOCÊ VENCEU! \nVamos jogar novamente...')
    vitorias += 1
    print('-=' * 15)

print(f'GAME OVER! Você venceu {vitorias} vezes.')
