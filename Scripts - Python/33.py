print('='*22)
print('Analisador de números')
print('='*22)
a= int(input('Digite um número: '))
b= int(input('Digite outro número: '))
c= int(input('Digite outro número: '))
maior = a
if b>a and b>c:
   maior = b
if c>a and c>b:
    maior = c
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('='*22)
print('O maior número é {} e o menor número é {}'.format(maior,menor))
