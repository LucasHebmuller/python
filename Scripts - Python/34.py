s= float(input('Qual é o salário do funcionário? '))
if s<=1250:
    print('Esse funcionário terá um aumento de 15% em seu salário, ficando assim com um salário de {} reais.'.format(s*115/100))
else:
    print('Esse funcionário terá um aumento de 10% em seu salário, ficando assim com um salário de {} reais.'.format(s*110/100))
