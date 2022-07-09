d= int(input('Qual a distancia da sua vigem, em Km? '))
if d<=200:
    print('A sua viagem vai custar {} reais'.format(d*0.5))
else:
    print('A sua viagem vai custar {} reais'.format(d*0.45))
