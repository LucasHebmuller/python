n1= int(input('Digite um numero: '))
n2= int(input('Digite mais um numero: '))
print('''Menu de opcoes:
    [1] Somar
    [2] Multiplicar
    [3] Dividir
    [4] Escolher novos numeros
    [5] Sair ''')
opc= int(input('Qual a sua opcao? '))
while opc!=5:
    if opc==1:
        print('A soma vale {}'.format(n1+n2))
    elif opc==2:
        print('A multiplicacao vale {}'.format(n1*n2))
    elif opc==3:
        print('A divisao vale {:.2f}'.format(n1/n2))
    elif opc==4:
        n1= int(input('Digite um numero: '))
        n2= int(input('Digite mais um numero: '))
    else:
        print('Opcao invalida, tente novamente')
    print('='*30)
    print('''Menu de opcoes:
    [1] Somar
    [2] Multiplicar
    [3] Dividir
    [4] Escolher novos numeros
    [5] Sair ''')
    opc= int(input('Qual a sua opcao? '))
print('Fim')
    
