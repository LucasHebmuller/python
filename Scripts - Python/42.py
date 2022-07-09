a= float(input('Qual é a medida do primeiro lado do triangulo? '))
b= float(input('Qual é a medida do segundo lado do triangulo? '))
c= float(input('Qual é a medida do terceiro lado do triangulo? '))
if a+b>c and a+c>b and b+c>a:
    print('Com essas medidas é possível formar um triângulo')
    if a==b==c:
        print('Esse é um triângulo equilatero')
    elif a==b or b==c or c==a:
        print('Esse é um triângulo isósceles')
    else:
        print('Esse e um triangulo escaleno')
else:
    print('Com essas medidas nao e possivel formar um triangulo')
