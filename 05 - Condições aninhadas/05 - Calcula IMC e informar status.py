#Crie um programa que leia o peso e altura de uma pessoa e calcule seu IMC e informe seu status:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#Entre 25 e 30: Sobrepeso
#Entre 30 e 40: Obeso
#Acima de 40: Obesidade morbida
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura ** 2
print('Seu imc é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25.0:
    print('Voce esta com peso ideal')
elif 25.0 <= imc < 30.0:
    print('Voce esta com sobrepeso')
elif 30.0 <= imc < 40.0:
    print('Voce está obeso')
else:
    print('Você está com obesidade morbida')
