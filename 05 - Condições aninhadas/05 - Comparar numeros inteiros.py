#Escreva um programa que leia dois numeros inteiros e compare-os, mostrando:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe numero maior, os dois sao igual
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
if num1 < num2:
    print('O primeiro numero é menor que o segundo')
elif num2 < num1:
    print('O segundo numero é menor que o primeiro')
else:
    print('Os dois numeros são iguais')