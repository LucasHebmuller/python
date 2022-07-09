n1= float(input('Qual e a primeira nota do aluno? '))
n2= float(input('Qual e a segunda nota do aluno? '))
m =(n1+n2)/2
if m>=7:
    print('O aluno esta aprovado')
elif m>=5 and m<7:
    print('O aluno esta em recuperacao')
else:
    print('O aluno esta reprovado')
