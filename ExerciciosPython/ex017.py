from math import hypot, sqrt
print('===== DESAFIO 017 =====\n')
coposto = float(input('Comprimento do cateto oposto: '))
cadjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(coposto, cadjacente)
hipot = sqrt((coposto ** 2) + (cadjacente ** 2))
# Feito utilizando o próprio método de hipotenusa da biblioteca:
print(f'O comprimento da hipotenusa desse triângulo é {hipotenusa:.2f}')
# Feito utilizando a fórmula da hipotenusa juntamente da raiz quadrada da biblioteca:
print(f'O comprimento da hipotenusa desse triângulo é {hipot:.2f}')