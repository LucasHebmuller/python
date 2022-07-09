listagem=('Agua',2,'Bala',0.05,'Pao',1,'Carne',20)
print('-'*40)
print('{:^40}'.format('Listagem de Precos'))
print('-'*40)
for pos in range(0,len(listagem)):
    if pos%2==0:
        print('{:.<30}'.format(listagem[pos]), end= ' ')
    else:
        print('{:>5}'.format(listagem[pos]))
print('-'*40)
