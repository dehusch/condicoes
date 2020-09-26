#Ler um numero e caso positivo:
#calcular a raiz e ao quadrado
num1 = float(input('Digite um numero: '))
if num1 > 0:
    num1 = num1 ** 2
    print(f'Elevado ao quadrado é: {num1}')
if num1 > 0:
    num1 = num1 ** (1/2)
    print(f'A raiz é: {num1}')
