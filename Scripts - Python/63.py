a= 0
b= 1
c= 0
x= 0
print('='*20)
print('{:^20}'.format('Fibonacci'))
print('='*20)
q= int(input('Quantos numeros voce quer mostrar? '))
print('{}'.format(a), end=' ')
print('{}'.format(b), end=' ')
while x<=q-3:
    x+= 1
    c = a+b
    print('{}'.format(c), end= ' ')
    a=b
    b=c
    
    
    
