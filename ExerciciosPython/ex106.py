def titulo(txt, cor='limpa'):
    tamanho = len(txt) + 4
    print(cores[cor], end='')
    print('~' * tamanho)
    print(f'  {txt}')
    print('~' * tamanho)
    print(cores['limpa'], end='')


def ajuda(obj):
    from time import sleep
    titulo(f'Acessando o manual do comando \'{obj}\'', 'azul')
    sleep(0.5)
    print(cores['branco'], end='')
    help(obj)
    print(cores['limpa'], end='')


# Programa Principal
cores = {'limpa': '\033[m',
         'branco': '\033[7;30m',
         'vermelho': '\033[1;30;41m',
         'verde': '\033[1;30;42m',
         'amarelo': '\033[1;30;43m',
         'azul': '\033[1;30;44m',
         'roxo': '\033[1;30;45m',
         'safira': '\033[1;30;46m',
         'cinza': '\033[1;30;47m'}

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 'verde')
    opcao = str(input('Função ou Biblioteca > ')).lower().strip()
    if opcao == 'fim':
        titulo('ATÉ LOGO!', 'vermelho')
        break
    ajuda(opcao)
