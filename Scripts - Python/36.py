print('-='*12)
print(' Analise de emprestimo')
print('-='*12)
casa= float(input('Qual e o preco da casa? '))
salario= float(input('Qual e o seu salario mensal? '))
tempo= int(input('Em quantos anos voce vai pagar esse emprestimo? '))
parcela= casa/(tempo*12)
minimo= salario*130/100
if parcela>minimo:
    print('Desculpe, mas voce nao pode pegar esse emprestimo.')
else:
    print('O emprestimo esta liberado, as parcelas sao de {:.2f} reais'.format(parcela))

