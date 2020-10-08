from time import sleep


# Definindo a função "maior()"
def maior(*num):
    maiornum = 0
    print('-=' * 30)
    print('Analisando os valores passados...')

    for numatual in num:
        if maiornum == 0 or numatual > maiornum:
            maiornum = numatual
        print(numatual, end=' ')
        sleep(0.5)

    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maiornum}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
