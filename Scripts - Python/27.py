nome= str(input('Digite o seu nome completo: ')).strip()
n= nome.split()
print('Seu primeiro nome e: {}'.format(n[0]))
print('Seu ultimo nome e: {}'.format(n[len(n)-1]))
