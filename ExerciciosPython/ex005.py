print('===== DESAFIO 005 =====\n')
n = int(input('Digite um valor: '))
print(f'----- NÚMERO \033[4m{n}\033[m -----')
print(f'Número antecessor: \033[31m{n - 1}\033[m')
print(f'Número sucessor: \033[36m{n + 1}')
