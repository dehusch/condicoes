#Create a list and pick odds and evens in another list
numbers = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numbers:
        numbers.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Digite novamente')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print(numbers)
even = list()
odd = list()
for i, v in enumerate(numbers):
    if v % 2 == 0:
        even.append(v)
    elif v % 2 == 1:
        odd.append(v)
print(f'Os numeros pares são: {even}')
print(f'Os numeros impares são: {odd}')
print('FIM')
