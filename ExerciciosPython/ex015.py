print('===== DESAFIO 015 =====\n')
dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
p = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${p:.2f}')
