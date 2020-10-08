from time import sleep # Importando a função para fazer o programa esperar
valorcasa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o valor do seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = valorcasa / (12 * anos) # Valor da prestação obtendo-se a quantidade de anos
print('\n\033[1;30;41mP R O C E S S A N D O . . .\033[m\n')
sleep(1) # O programa vai esperar por 1 segundo
if valorcasa <= 0 or salario <= 0 or anos <= 0: # Verifica se foi digitado números negativos ou iguais a 0
    print('\033[31mE R R O R  4 2 \nVALORES INVÁLIDOS!')
elif prestacao > (salario * 0.3): # Verifica se o valor da prestação é MAIOR do que 30% do salário
    print(f'\033[31mEMPRÉSTIMO NEGADO! \nO valor da prestação será R${prestacao:.2f}')
    print('O valor é muito alto para sua faixa salarial!')
else: # Bloco executável caso o valor da prestação seja MENOR do que 30% do salário
    print(f'\033[34mEMPRÉSTIMO APROVADO! \nO valor da prestação será R${prestacao:.2f}')
    print('Contate o gerente para finalizar o processo.')
print('\n\033[1;30;41mE N C E R R A N D O . . .\033[m')
