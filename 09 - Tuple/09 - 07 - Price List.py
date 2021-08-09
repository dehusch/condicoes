#Create a price list with tuple
lista = 'Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}', end='')
    else:
        print(f'R${lista[pos]:>5}')
print('FIM')