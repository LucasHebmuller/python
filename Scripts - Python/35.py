print('-='*12)
print('Analisador de triângulos')
print('-='*12)
a= float(input('Digite um lado do triângulo: '))
b= float(input('Digite outro lado do triângulo: '))
c= float(input('Digite outro lado do triângulo: '))
if a<b+c and b<a+c and c<a+b:
    print('Pode ser formado um triângulo com essas medidas.')
else:
    print('Não pode ser formado um triângulo com essas medidas.')
