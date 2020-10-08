valor = float(input('Valor do produto --> R$'))
print('\033[34m----- ESCOLHA A FORMA DE PAGAMENTO: -----')
print('\033[1;30m[1] À VISTA DINHEIRO/CHEQUE')
print('\033[1;36m[2] À VISTA NO CARTÃO')
print('\033[1;32m[3] EM ATÉ 2X NO CARTÃO')
print('\033[1;33m[4] 3X OU MAIS NO CARTÃO')
print('\033[34m-' * 42, '\033[m')
pagamento = int(input(''))
if pagamento == 1: # Verifica se o usuário escolheu a opção de pagamento 1 (à vista no dinheiro/cheque)
    print('FORMA DE PAGAMENTO: \033[1;30mÀ VISTA DINHEIRO/CHEQUE\033[m')
    print('DESCONTO DE 10%')
    print(f'VALOR FINAL DO PRODUTO: R${valor - (valor * 0.10):.2f}')
elif pagamento == 2: # Verifica se o usuário escolheu a opção de pagamento 2 (à vista no cartão)
    print('FORMA DE PAGAMENTO: \033[1;36mÀ VISTA NO CARTÃO\033[m')
    print('DESCONTO DE 5%')
    print(f'VALOR FINAL DO PRODUTO: R${valor - (valor * 0.05):.2f}')
elif pagamento == 3: # Verifica se o usuário escolheu a opção de pagamento 3 (em até 2x no cartão)
    print('FORMA DE PAGAMENTO: \033[1;32mEM ATÉ 2X NO CARTÃO\033[m')
    print('PREÇO NORMAL')
    print(f'VALOR FINAL DO PRODUTO: R${valor:.2f}')
    print(f'PARCELAS: 2X DE R${valor / 2:.2f}')
elif pagamento == 4: # Verifica se o usuário escolheu a opção de pagamento 4 (3x ou mais no cartão)
    parcelas = int(input('Quantas parcelas? '))
    if parcelas < 3:
        print('\033[1;31mERRO: O NÚMERO DE PARCELAS NÃO PODE SER MENOR DO QUE 3')
    else:
        print('FORMA DE PAGAMENTO: \033[1;33m3X OU MAIS NO CARTÃO\033[m')
        print('20% DE JUROS')
        print(f'VALOR FINAL DO PRODUTO: R${valor * 1.20:.2f}')
        print(f'PARCELAS: {parcelas}X DE R${(valor * 1.20) / parcelas:.2f}')
else: # Bloco executável caso o usuário coloque uma forma de pagamento diferente de 1, 2, 3 ou 4
    print('\033[1;31mERRO: DÍGITO INVÁLIDO! \nTENTE NOVAMENTE.')
