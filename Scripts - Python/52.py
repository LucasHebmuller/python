div= 0
n= int(input('Digite um numero: '))
for c in range(1,n+1):
    if n%c==0:
        div= div + 1
if div==2:
    print('Esse numero e primo')
else:
    print('Esse numero nao e primo')
