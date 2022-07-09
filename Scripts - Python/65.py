maior = 0
menor = 99999999999999999999999999999999999999999999999999999999
n= int(input('Digite um número: '))
r = str(input('Vc quer continuar? [S/N] ')).strip().upper()
m = n
c = 1
while r!='N':
    n= int(input('Digite um número: '))
    m+= n
    c+= 1
    if n> maior:
        maior = n
    if n<menor:
        menor = n
    r = str(input('Vc quer continuar? [S/N] ')).strip().upper()
print('''Programa finalizado.
     {} numeros foram digitados e a media entre eles foi {:.1f}.'''.format(c, m/c))
print('O maior numero digitado foi {} e o menor {}'.format(maior,menor))
    
    
    
    
