v= int(input('Qual a velocide atual do carro? '))
l= 80
c= v-l
if v>80:
    print('Multado! Voce esta acima do limite de velocidade e tera que pagar uma multa de {} reais'.format(c*7))
else:
    print('Tenha um bom dia! Dirija com seguranca!')
    
