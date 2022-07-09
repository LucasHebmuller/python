def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f
n = int(input('Digite um numero: '))
print('O fatorial de {} é {}'.format(n, fatorial(n)))
