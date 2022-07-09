s= 0
for c in range(0,5):
    n= int(input('Digite um numero inteiro: '))
    if n%2==0:
        s+= n
print('A soma dos numeros pares foi: {}'.format(s))
