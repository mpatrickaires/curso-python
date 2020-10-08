numero = int(input('Digite um número para calcular seu fatorial --> '))
fatorial = numero
if numero == 0 or numero == 1:
    print(f'{numero}! = 1')
else:
    print(f'{numero}! = {numero} x ', end='')
    while numero >= 1:
        numero = numero - 1
        fatorial = fatorial * numero
        if numero != 1:
            print(f'{numero} x ', end='')
        else:
            print(f'{numero} = {fatorial}')
            numero = numero - 1
