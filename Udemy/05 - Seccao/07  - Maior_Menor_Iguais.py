num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
maior = num1
if num1 > num2:
    maior = num1
    print(f'Este é o numero maior{maior}')
if num2 > num1:
    maior = num2
    print(f'Este é o numero maior {maior}')
if num1 == num2:
    print('Os dois numeros digitados são iguais')