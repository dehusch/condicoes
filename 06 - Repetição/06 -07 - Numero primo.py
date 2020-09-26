#Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo
#o valor de if deve ser ou 1 ou o numero digitado
num = int(input('Digite um valor inteiro para saber se é um numero primo: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont = cont + 1 #Aqui conta quantas vezes o IF do laço acontece
if cont == 2:
    print('Este é um numero primo')
else:
    print('Este não é um numero primo')
