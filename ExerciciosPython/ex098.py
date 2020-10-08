from time import sleep


# Definindo a Função contador()
def contador(a, b, c):
    print('-=' * 20)
    if c == 0:
        c = 1
    if c < 0:
        c = abs(c)
    print(f'Contagem de {a} até {b} de {c} em {c}')

    if a < b:  # Verifica se o início é menor que o fim para fazer uma contagem sucessiva
        for i in range(a, b + 1, c):
            print(i, end=' ')
            sleep(0.5)

    else:  # Contagem regressiva, indicando que o início é maior que o fim
        for i in range(a, b - 1, - c):
            print(i, end=' ')
            sleep(0.5)

    print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, - 2)

print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)
