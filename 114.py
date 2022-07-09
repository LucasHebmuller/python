import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('O site nao esta acessivel no momoneto')
else:
    print('Consegui acessar o site')
