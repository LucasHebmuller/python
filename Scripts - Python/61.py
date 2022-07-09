c= 10
print('='*30)
print('{:^30}'.format('Gerador de PA'))
print('='*30)
n= int(input('Por qual numero comeca a PA? '))
r= int(input('Qual a razao da PA? '))
while c>0:
    print('{}->'.format(n), end=' ')
    n+= r
    c-= 1
print('Fim')
