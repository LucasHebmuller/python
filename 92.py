lista = {}
lista['Nome'] = str(input('Nome: '))
lista['Idade'] = int(input('Idade: '))
lista['Cpts'] = int(input('Carteira de Trabalho (0 nao tem): '))
if lista['Cpts'] != 0:
    lista['Contratacao'] = int(input('Ano de contratacao: '))
    lista['Salario'] = int(input('Salario: R$'))
    lista['Aposentadoria'] = 65-lista['Idade']
for k,v in lista.items():
    print(f' {k} é {v}')
