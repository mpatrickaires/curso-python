opcao = 'S'
lista = []

while opcao == 'S':
    n = int(input('Digite um número --> '))
    lista.append(n)
    opcao = str(input('Deseja continuar [S/N]? ')).strip().upper()

    while opcao != 'S' and opcao != 'N':
        print('\033[1;31mERRO: OPÇÃO INVÁLIDA! TENTE NOVAMENTE COM "S" OU "N"!\033[m')
        opcao = str(input('Deseja continuar [S/N]? ')).strip().upper()

print(f'''\033[1;36mMÉDIA DOS VALORES DIGITADOS --> {sum(lista) / len(lista)}
MAIOR VALOR DIGITADO --> {max(lista)}
MENOR VALOR DIGITADO --> {min(lista)}''')
