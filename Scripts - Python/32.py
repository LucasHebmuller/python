ano= int(input('Para descobrir se algum ano é bissexto, basta digitá-lo aqui: '))
if (ano%4)==0:
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} nao é um ano bissexto.'.format(ano))
