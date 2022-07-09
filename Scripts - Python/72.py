numeros= ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
n= int(input('Digite um numero entre 0 e 10: '))
if n>=0 and n<=10:
    print('Voce digitou o numero {}.'.format(numeros[n]))
else:
    print('Opcao invalida. Tente novamente. ')
