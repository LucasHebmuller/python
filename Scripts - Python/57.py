sexo= str(input('Qual é o sexo da pessoa analisada? [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    print('O dado fornecido foi invalido, tente novamente.')
    sexo= str(input('Qual é o sexo da pessoa analisada? [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))    
