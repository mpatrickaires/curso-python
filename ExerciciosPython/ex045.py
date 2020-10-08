from random import randint # Importa o randomizador da biblioteca RANDOM
from time import sleep # Importa a função para o programa esperar da biblioteca TIME
computador = randint(0, 2) # Faz o computador escolher um número aleatório de 1 até 3
jogadas = ['Pedra', 'Papel', 'Tesoura']
print('\033[1;30m===== \033[4;30mJ O K E N P Ô\033[0;30m =====')
print('\033[1;34m[0] PEDRA')
print('\033[1;35m[1] PAPEL')
print('\033[1;36m[2] TESOURA')
print('\033[1;30m=' * 25)
usuario = int(input('ESCOLHA SUA JOGADA --> '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
if usuario == 0 or usuario == 1 or usuario == 2: # Verifica se o fez uma jogada válida
    print('-=' * 12)
    print(f'Computador jogou {jogadas[computador]} \nUsuário jogou {jogadas[usuario]}')
    print('-=' * 12)
# Verifica se o usuário venceu:
if (usuario == 0 and computador == 2) or (usuario == 1 and computador == 0) or (usuario == 2 and computador == 1):
    print('\033[1;32mPARABÉNS! Você venceu!')
# Verifica se o computador venceu:
elif (computador == 0 and usuario == 2) or (computador == 1 and usuario == 0) or (computador == 2 and usuario == 1):
    print('\033[1;31mVOCÊ PERDEU! Sinto muito...')
# Verifica se houve empate:
elif usuario == computador:
    print('\033[1;37mOPA! Temos um empate!')
# Verifica se o usuário digitou um número diferente de 1, 2 ou 3:
else:
    print('\033[31mERRO: DIGITE UMA JOGADA VÁLIDA!')
