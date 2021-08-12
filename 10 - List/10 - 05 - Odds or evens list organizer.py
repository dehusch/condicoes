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
even = numbers[:]
odd = numbers[:]
for c in even:
    if c % 2 == 1:
        even.remove(c)
for c in odd:
    if c % 2 == 0:
        odd.remove(c)
print(f'Os numeros pares são: {even}')
print(odd)
print('FIM')
