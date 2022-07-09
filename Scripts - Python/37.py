n= int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases de conversao:
[ 1 ] para BINARIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL''')
opcao= int(input('Qual sua escolha? '))
if opcao==1:
    print('{} convertido para binario fica {}'.format(n, bin(n)))
elif opcao==2:
    print('{} convertido para octal fica {}'.format(n, oct(n)))
elif opcao==3:
    print('{} convertido para hexadecimal fica {}'.format(n, hex(n)))
else:
    print('Voce nao escolheu uma das opcoes ')
