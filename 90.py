aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Nota'] = int(input('Nota: '))
if aluno['Nota'] < 5:
    aluno['Situacao'] = 'reprovado'
elif aluno['Nota'] < 7:
    aluno['Situacao'] = 'recuperacao'
else:
    aluno['Situacao'] = 'aprovado'
print('='*20)
for keys, values in aluno.items():
    print(f'{keys} é igual a {values}')
