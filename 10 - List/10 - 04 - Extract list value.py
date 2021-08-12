#Show an list numbers em check if a specific number contains in list
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
if 5 in numbers:
    print("O numero 5 faz parte da lista")
else:
    print(f'Não achei o numero 5 na lista')
numbers.sort()
print(f'Os valores em ordem crescente são: {numbers}')
