print('-' * 40)
print(f'{"LOJA SUPER BARATÃO":^40}')
print('-' * 40)
mais_de_1000 = total_compra = preco_produto_mais_barato = 0
nome_produto_mais_barato = ''

while True:
    produto_atual = str(input('Nome do Produto: ')).title().strip()
    preco_atual = float(input('Preço: R$'))
    while preco_atual <= 0:
        preco_atual = float(input('Preço: R$'))

    if preco_produto_mais_barato == 0 or preco_atual < preco_produto_mais_barato:
        preco_produto_mais_barato = preco_atual
        nome_produto_mais_barato = produto_atual

    if preco_atual > 1000:
        mais_de_1000 += 1

    total_compra += preco_atual

    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opcao == 'N':
        break

print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'''Total da compra --> R${total_compra:.2f}
Total de produtos custando mais de R$1000.00 --> {mais_de_1000}
O produto mais barato foi {nome_produto_mais_barato} que custa R${preco_produto_mais_barato:.2f}''')
print('-' * 40)
