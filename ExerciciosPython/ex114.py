import urllib.request

try:
    urllib.request.urlopen("http://www.pudim.com.br/").getcode()
    print('\033[1;32mConsegui acessar o site Pudim com sucesso!\033[m')
except:
    print('\033[1;31mO site Pudim não está acessível no momento.\033[m')
