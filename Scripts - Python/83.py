exp= str(input('Digite uma expressao aritmetica: '))
x = exp.count('(')
y = exp.count(')')
if x == y:
    print('Essa expressao e valida')
else:
    print('Essa expressao nao e valida')
    
