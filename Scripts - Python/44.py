p= float(input('Qual o preco do produto que voce quer comprar, em reais? '))
opcao= int(input('''Digite a sua escolha de forma de pagamento:
[ 1 ] a vista em dinheiro ou em cheque
[ 2 ] a vista no cartao
[ 3 ] em ate 2x no cartao
[ 4 ] em 3x ou mais no cartao '''))
if opcao==1:
    print('Por escolher essa opcao de pagamento, voce recebeu um desconto de 10%, assim sua compra sai por {} reais.'.format(p*90/100))
elif opcao==2:
    print('Por escolher essa opcao de pagamento, voce recebeu um desconto de 5%, assim sua compra sai por {} reais.'.format(p*95/100))
elif opcao==3:
    print('A sua compra sai pelo preco normal, {} reais'.format(p))
elif opcao==4:
    print('Devido a sua escolha de forma de pagamento, sua compra vai sair com juros de 20%, ficando assim {} reais.'.format(p*120/100))
else:
    print('Voce nao escolheu nenhuma opcao de pagamento disponivel')
    
