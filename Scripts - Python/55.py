maior=0
menor=999999999999999999999999
for c in range(1,6):
    peso= float(input('Digite o peso de cinco pessoas: '))
    if peso>maior:
        maior = peso
    if peso<menor:
        menor = peso
print('O maior peso digitado foi {} e o menor foi {}'.format(maior,menor))
