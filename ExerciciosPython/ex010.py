print('===== DESAFIO 010 =====\n')
r = float(input('Digite o valor que você possui em reais: R$'))
d = r / 5.31
e = r / 5.98
i = r / 0.0494
print(f'Valor que você pode comprar em dólares: US${d:.2f}')
print(f'Valor que você pode comprar em euros: €{e:.2f}')
print(f'Valor que você pode comprar em iênes: ¥{i:.2f}')
