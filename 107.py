import moeda
p = float(input('Digite um preco: R$'))
print(f'A metade de {p} vale {moeda.metade(p)}')
print(f'O dobro de {p} vale {moeda.dobro(p)}')
print('Aumentando 10%, temos {}'.format(moeda.aumentar(p,10)))
print('Diminuindo 10%, temos {}'.format(moeda.diminuir(p,10)))
