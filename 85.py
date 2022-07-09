valores = [[],[]]
for c in range(1,8):
    n = int(input(f'Digite o {c} valor: '))
    if n%2!=0:
        valores[1].append(n)
    else:
        valores[0].append(n)
valores[1].sort()
valores[0].sort()
print('|'*20)
print(f'Os valores pares sao: {valores[0]}')
print(f'Os valores impares sao: {valores[1]}')
