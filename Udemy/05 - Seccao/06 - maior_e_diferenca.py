num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
maior = num1
if num1 > num2:
    maior = num1
    print(maior)
if num2 > num1:
    maior = num2
    print(maior)
print(f'A diferenca entre os dois numeros é de {num1 - num2}')