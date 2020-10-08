def leiadinheiro(texto):
    valor = str(input(texto))
    while not valor.replace(',', '').isnumeric():
        print(f'\033[1;31mERRO: "{valor}" é um preço inválido!\033[m')
        valor = input(texto)
    return float(valor)
