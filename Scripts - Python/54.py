maior=0
menor=0
for c in range(1,8):
    ano_nasc= int(input('Digite o ano de nascimento de sete pessoas? '))
    if 2022-ano_nasc>=18:
        maior += 1
    else:
        menor += 1
print('Dessas pessoas, {} sao maiores de idade e {} nao'.format(maior,menor))
    
