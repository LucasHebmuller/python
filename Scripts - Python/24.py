city= input('Em que cidade tu nasceste? ').strip()
print('Analisando o nome dessa cidade, sera que o nome dela comeca com Santo?')
x= city.upper()
r= 'SANTO' in x[:5]
print (r)
