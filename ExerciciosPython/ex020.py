from random import sample, shuffle
print('===== DESAFIO 020 =====')
aluno1 = input('1º Aluno: ')
aluno2 = input('2º Aluno: ')
aluno3 = input('3º Aluno: ')
aluno4 = input('4º Aluno: ')
#Para montar listas, é preciso fazer o uso de --> []
#Só para lembrar: ( ) --> parênteses; [ ] --> colchetes; { } --> chaves
lista = [aluno1, aluno2, aluno3, aluno4]
#Para utilizar shuffle é preciso realizar o comando antes do print
shuffle(lista)
#Utilizando o comando ~sample~:
print(f'Ordem de apresentação: {sample(lista, k=4)}') #O ~k~ é a quantidade de elementos da lista que vão aparecer
#Utilizando o resultado obtido do comando ~shuffle~:
print(f'Ordem de apresentação: {lista}')
