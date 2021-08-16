#create a matrix 3x3
#calc sum the evens numbers
#calc sum from third colunn
#highest number from second line
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sumevens = high = sumcolunn = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor na posicao [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='') #^5 center the text inside 5 spaces
        if matrix[l][c] % 2 == 0:
            sumevens = sumevens + matrix[l][c]
    print()
print(f'A soma dos valores pares é {sumevens}')
for l in range(0, 3):
    sumcolunn = sumcolunn + matrix[l][2] #Calculated only the lines from colunn 2
print(f'A soma da terceira coluna é {sumcolunn}')
for c in range(0, 3):
    if c == 0:
        high = matrix[1][c]
    elif matrix[1][c] > high:
        high = matrix[1][c]
print(f'O maior numero da segunda coluna é {high}')
