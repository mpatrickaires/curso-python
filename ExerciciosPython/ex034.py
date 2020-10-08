salario = float(input('Digite o seu salário --> R$'))
aumento = salario * 0.15
if salario > 1250:
    aumento = salario * 0.10
print(f'-----    SALÁRIO   -----> R${salario:.2f}')
print(f'-----    AUMENTO   -----> R${aumento:.2f}')
print(f'----- NOVO SALÁRIO -----> R${salario + aumento:.2f}')
