def contador(a,b,c):
    print('='*35)
    print('Contagem de {} ate {} de {} em {}:'.format(a,b,c,c))
    if a < b:
        while True:
            print(a, end=' ')
            a += c
            if a > b:
                break
    elif a > b:
        while True:
            print(a, end=' ')
            a -= c
            if b > a:
                break
    else:
        print('ERRO! Tente novamente.')
    print()        
    print('='*35)


contador(1,10,1)
contador(20,0,4)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passo: '))
if p < 0:
    p = (p*-1)
contador(i,f,p)

            
            
        
