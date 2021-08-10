#Add N numbers in a list, reject same numbers and give the option to stop the list
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
numbers.sort()
print(f'Os valores em ordem crescente são: {numbers}')
