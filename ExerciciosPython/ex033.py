numero1 = float(input('Digite o 1º número --> '))
numero2 = float(input('Digite o 2º número --> '))
numero3 = float(input('Digite o 3º número --> '))
print('UTILIZANDO ~if~:')
# Verificando quem é o MAIOR
if (numero1 >= numero2) and (numero1 >= numero3):
    maiornumero = numero1
if (numero2 >= numero1) and (numero2 >= numero3):
    maiornumero = numero2
if (numero3 >= numero1) and (numero3 >= numero2):
    maiornumero = numero3
# Verificando quem é o MENOR
if (numero1 <= numero2) and (numero1 <= numero3):
    menornumero = numero1
if (numero2 <= numero1) and (numero2 <= numero3):
    menornumero = numero2
if (numero3 <= numero1) and (numero3 <= numero2):
    menornumero = numero3
print(f'O maior número é {maiornumero} e o menor número é {menornumero}\n')
print('UTILIZANDO LISTA COM ~max()~ E ~min()~:')
# Montando uma LISTA
listanumeros = [numero1, numero2, numero3]
print(f'O maior número é {max(listanumeros)} e o menor número é {min(listanumeros)}\n')
print('UTILIZANDO LISTA COM ~sorted()~:')
# Ordenando a lista do MENOR para o MAIOR
listanumeros_ordenado = sorted(listanumeros)
print(f'O maior número é {listanumeros_ordenado[2]} e o menor número é {listanumeros_ordenado[0]}')
