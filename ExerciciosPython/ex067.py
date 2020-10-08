while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)

    if valor < 0:  # Programa encerra quando o número digitado for negativo
        break

    for tabuada in range(1, 11):
        print(f'{valor} x {tabuada:<2} = {valor * tabuada}')
    print('-' * 30)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
