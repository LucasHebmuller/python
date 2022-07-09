print('Tabuada (Digite um valor negativo para parar)')
print('='*30)
n=0
while True:
    n=int(input('Digite um valor: '))
    if n<0:
        print('='*30)
        break
    for c in range (1,11):
        print(f'{n} x {c} = {n*c}')
    print('='*30)
print('Programa finalizado')
