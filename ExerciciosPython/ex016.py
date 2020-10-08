from math import trunc
print('===== DESAFIO 016 =====\n')
num = float(input('Digite um número: '))
# Utilizando importação:
print(f'O número {num} tem a parte inteira {trunc(num)}')
# Utilizando a formatação do número para inteiro:
print(f'O número {num} tem a parte inteira {int(num)}')
