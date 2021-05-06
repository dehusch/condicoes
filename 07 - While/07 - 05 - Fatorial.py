#Calcular fatorial
#Fatorial de 5! é 5x4x3x2x1
from math import factorial
fac = int(input('Digite um numero: '))
f = factorial(fac)
print(f'O fatorial de {fac} é {f}')

#=============================================

#calcular com while
from math import factorial
n = int(input('Digite um numero: '))
c = n
fa = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fa = fa * c
    c = c - 1
print(f'{fa}')

#outra forma
numfac = int(input('Digite um numero para saber seu fatorial: '))
cn = numfac
fat = 1
while cn > 0:
  fat = fat * cn
  cn = cn - 1
print(fat)
print('FIM')
