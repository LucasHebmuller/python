print('{:^30}'.format('Cadastramento de pessoas'))
print('='*30)
maior = masc = fem20 = i = s = 0
r='s'
while True:
    i= int(input('Qual a idade da pessoa? '))
    s= str(input('Qual o sexo da pessoa? [m/f] ')).lower().strip()
    if i>18:
        maior+= 1
    if s=='m':
        masc+= 1
    if s=='f' and i<20:
        fem20+= 1
    r= str(input('Voce quer continuar? [s/n] ')).lower().strip()
    if r=='n':
        break
    elif r!='n' and r!='s':
        print('Erro. Tente novamente')
    print('='*30)
print('Cadastramento finalizado')
print(f'Ha {maior} pessoas maiores de 18 anos,{fem20} mulheres com menos de vinte anos e {masc} homens')
    
    
