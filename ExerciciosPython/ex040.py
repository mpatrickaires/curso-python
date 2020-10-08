nota1 = float(input('1ª Nota --> '))
nota2 = float(input('2ª Nota --> '))
media = (nota1 + nota2) / 2
if nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0: # Verifica se o usuário digitou valores maiores que 10 ou negativos
    print('\033[31mERRO: VALORES INVÁLIDOS \nAS NOTAS NÃO PODEM SER MAIORES QUE 10 OU NEGATIVAS!')
elif media < 5: # Verifica se a média é menor que 5
    if media == 4.95: # Transforma 4.95 em 4.9 pois o Python arredonda 4.95 para 5, gerando inconsistência no resultado
        media = 4.9
    print(f'Média   --> {media:.1f} \n\033[31mALUNO REPROVADO')
elif media < 7: # Verifica se a média é menor que 7, logicamente representando que é maior que 5 e menor que 7
    print(f'Média   --> {media:.1f} \n\033[33mALUNO DE RECUPERAÇÃO')
else: # Bloco executável caso a nota seja maior ou igual a 7
    print(f'Média   --> {media:.1f} \n\033[36mALUNO APROVADO')
