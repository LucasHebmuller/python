def fatorial(n):
    f = 1
    c = n
    while c > 0:
        if c > 1:
            print(f'{c} x ',end='')
        else:
            print(f'{c} ',end='')
        f *= c
        c -= 1
    print(f'= {f}')
    
              
fatorial(6)
