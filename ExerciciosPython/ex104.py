def leiaInt(msg):
    num = str(input(msg))
    while not num.strip('-').isnumeric():
        print('\033[1;31mERRO! Digite um número válido.\033[m')
        num = input(msg)
    num = int(num)
    return num


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
