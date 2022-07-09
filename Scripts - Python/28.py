from random import randint
print('Vou pensar entre 0 e 5. Tente adivinhar...')
x= randint(0,5)
n= int(input('Qual e a sua aposta? '))
if n==x:
    print('Parabens! Voce adivinhou!')
else:
    print('Voce errou, eu pensei no numero {}'.format(x))

