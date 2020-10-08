numero = int(input('Digite um número --> '))
primo = 0
for c in range(1, numero + 1):
    if numero % c == 0:  # Checa se o número é primo ao realizar a divisão dele por todos os números de 1 até
        # o número digitado pelo usuário; se ao verificar o resto ele der 0, o número é divisível pelo valor c
        print(f'\033[1;33m{c}', end='\033[m ')
        primo = primo + 1  # Variável primo é somado com mais 1 caso seja divisível pelo valor c
    else:  # Bloco executável caso o número não seja divisível pelo valor c
        print(f'\033[1;31m{c}', end='\033[m ')
print(f'\nO número {numero} só foi divisível {primo} vezes')
if primo == 2:  # Verifica se o número é primo ao verificar se ele só foi dividido 2 vezes
    print(f'E por isso ele é PRIMO!')
else:  # Bloco executável caso a variável primo tenha sido dividido 3 vezes ou mais
    print(f'E por isso ele NÃO É PRIMO!')
