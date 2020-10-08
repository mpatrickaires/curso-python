soma = total = 0
n = int(input('Digite um número [999 para encerrar] --> '))
while n != 999:
    soma = soma + n
    total = total + 1
    n = int(input('Digite um número [999 para encerrar] --> '))
print(f'\033[1;32mTOTAL DE NÚMEROS DIGITADOS --> {total} \nSOMA DOS NÚMEROS DIGITADOS --> {soma}')
