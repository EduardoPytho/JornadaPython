import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro!')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())