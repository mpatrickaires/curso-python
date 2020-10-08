while True:
    try:
        numInt = int(input('Digite um Inteiro: '))
        break
    except ValueError:
        print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')

while True:
    try:
        numReal = float(input('Digite um Real: '))
        break
    except ValueError:
        print('\033[1;31mERRO: por favor, digite um número real válido.\033[m')
    except KeyboardInterrupt:
        numReal = 0
        print('\033[1;31mUsuário preferiu não digitar esse número.\033[m')
        break

print(f'O valor inteiro digitado foi {numInt} e o real foi {numReal}')
