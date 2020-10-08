from random import randint
from playsound import playsound
from time import sleep
NumeroComputador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
NumeroUsuario = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if NumeroUsuario == NumeroComputador:
    print('PARABÉNS! Você conseguiu me vencer!')
    playsound('ex028-acerto.mp3')
else:
    print(f'GANHEI! Eu pensei no número {NumeroComputador} e não no {NumeroUsuario}!')
    playsound('ex028-erro.mp3')
    sleep(1)
