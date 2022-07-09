print('='*20)
print('Calculo IMC')
print('='*20)
peso= float(input('Qual o seu peso, em Kg? '))
altura= float(input('Qual a sua altura em m? '))
IMC= peso/altura**2
print('='*20)
print('Seu IMC e {:.1f}'.format(IMC))
if IMC<18.5:
    print('Voce esta abaixo do peso')
elif IMC<=25:
    print('Voce esta com o peso normal')
elif IMC<30:
    print('Voce esta com sobrepeso')
elif IMC<40:
    print('Voce esta obeso')
else:
    print('Voce esta com obesidade morbida')
