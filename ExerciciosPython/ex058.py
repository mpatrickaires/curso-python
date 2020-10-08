from random import randint
from time import sleep
print('\033[1;33m-*-' * 14)
print('ESTOU PENSANDO EM UM NÚMERO DE 0 A 10...')
print('-*-' * 14)
sleep(1)
computador = randint(0, 10)
usuario = int(input('\033[mEm que número eu pensei? '))
tentativas = 1
while usuario != computador:
    if usuario > computador:
        print(f'\033[1;31mOps! Meu número é MENOR do que "{usuario}", tente novamente!\033[m')
    elif usuario < computador:
        print(f'\033[1;31mOps! Meu número é MAIOR do que "{usuario}", tente novamente!\033[m')
    tentativas = tentativas + 1
    usuario = int(input('Em que número eu pensei? '))
print(f'''\033[1;36mPARABÉNS, você acertou! Eu pensei no número "{computador}"!
Você precisou de \033[1;31m{tentativas}\033[1;36m tentativa(s) para acertar!''')
