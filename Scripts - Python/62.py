a=1
c= 1
print('='*30)
print('{:^30}'.format('Gerador de PA'))
print('='*30)
n= int(input('Por qual numero comeca a PA? '))
r= int(input('Qual a razao da PA? '))
while c<11:
    print('{}->'.format(n), end=' ')
    n+= r
    c+= 1
print('Pausa')
while a!=0:
    a= int(input('Quantos termos voce quer mostrar a mais? '))
    if c<a+1:
        print('{}->'.format(n), end=' ')
        n+= r
        c+= 1
print('Progressao finalizada')
print('{} termos da progressao foram mostrados'.format(c-1))
        
