x= 0
print('='*40)
print('{:^40}'.format('Os 10 primeiros termos de uma PA'))
print('='*40)
i= int(input('Por qual numero comeca a PA? '))
p= int(input('Qual o pulo? '))
for c in range(0,10):
    x= i + p*c
    print('{}'.format(x), end='->')
print('Acabou')
    
  
