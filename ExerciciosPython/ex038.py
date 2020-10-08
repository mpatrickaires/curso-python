n1 = int(input('Primeiro Valor --> '))
n2 = int(input('Segundo Valor  --> '))
if n1 > n2:
    print('O \033[36mPRIMEIRO VALOR\033[m é maior!')
elif n2 > n1:
    print('O \033[36mSEGUNDO VALOR\033[m é maior!')
else:
    print('Não existe valor maior, os dois são \033[36mIGUAIS\033[m!')
