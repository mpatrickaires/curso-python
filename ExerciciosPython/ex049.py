n = int(input('De que número você quer ver a tabuada? '))
print(f'===== TABUADA DE {n} =====')
for c in range(1, 11):
    print(f'{n} x {c:<2} = {n * c}')  # Mostra a multiplicação do número (n) pela posição de 'c' que vai te 1 a 10
print('=' * 24)
