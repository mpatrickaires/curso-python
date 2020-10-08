def area(a, b):
    calculo = a * b
    print(f'A área de um terreno {a}x{b} é de {calculo}m².')


# Programa Principal
print(f'{"Controle de terrenos":^30}')
print('-' * 30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
