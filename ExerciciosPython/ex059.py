from time import sleep
opcao = 0
valor1 = float(input('1º Valor --> '))
valor2 = float(input('2º Valor --> '))
while opcao != 5:
    print('''-------- MENU --------
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS VALORES
[5] SAIR DO PROGRAMA
----------------------''')
    opcao = int(input('Digite sua opção --> '))
    if opcao == 1:
        print(f'{valor1} + {valor2} = {valor1 + valor2}')
    elif opcao == 2:
        print(f'{valor1} X {valor2} = {valor1 * valor2}')
    elif opcao == 3:
        print(f'O maior valor é {max([valor1, valor2])}')
    elif opcao == 4:
        valor1 = float(input('1º Valor --> '))
        valor2 = float(input('2º Valor --> '))
    elif opcao == 5:
        print('E N C E R R A N D O . . .')
    else:
        print('ERRO: OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
    sleep(1.5)
