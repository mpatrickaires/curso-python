velocidade = int(input('Digite a velocidade do carro em Km/h --> '))
if velocidade < 0:
    print('VALOR INVÁLIDO! POR FAVOR, TENTE NOVAMENTE...')
elif velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado no valor de R${multa:.2f} por estar {velocidade - 80}Km/h acima do permitido!')
else:
    print('Sua velocidade está dentro do permitido!')
print('Tenha um bom dia! Dirija com segurança!')
