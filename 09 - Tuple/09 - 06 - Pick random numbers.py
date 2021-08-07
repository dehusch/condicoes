numbers = (int(input('DIgite um valor:')), int(input('DIgite um valor:')),
            int(input('DIgite um valor:')), int(input('DIgite um valor:')))
print(f'O numero 9 aparece {numbers.count(9)} vez(es)')
if 3 in numbers:
    print(f'O numero 3 aparece na posicao {numbers.index(3)}')
else:
    print('O valor 3 nao foi digitado')
if numbers[0] % 2 == 0:
    print(f'{numbers[0]} é um numero par')
if numbers[1] % 2 == 0:
    print(f'{numbers[1]} é um numero par')
if numbers[2] % 2 == 0:
    print(f'{numbers[2]} é um numero par')
if numbers[3] % 2 == 0:
    print(f'{numbers[3]} é um numero par')
print("FIM")
#
#Outro metodo
#
print('Os numeros pares são:')
for c in numbers:
    if c % 2 == 0:
        print(c, end=' ')
print('\nFIM')