#se o numero for positivo, imprimir a raiz
#se o numero for negativo, elevar ao quadrado
num1 = float(input('Digite um numero:'))
if num1 < 0:
    num1 = num1 ** 2
    print(num1)
else:
    num1 = num1 ** (1/2)
    print(num1)