#Para repetição de uma string definindo um limite
for c in range(0, 6): #c é a variavel, e pode ser definida qualquer uma.
    print('Ola')
print('Fim')
#Para contagem de 1 ate 6
for c in range(1, 7):
    print(c)
print('Fim')
#Para contagem de 6 ate 1
for c in range(6, 0, -1):
    print(c)
print('Fim')
#Contar de 2 em 2 ate 7
for c in range(0, 7, 2):
    print(c)
print('Fim')
#Digite um numero para fazer a contagem
n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('Fim')
#Digite o inicio o fim e o passo
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f, p):
    print(c)
print('Fim')
#repetição de input dentro de um for
for c in range(0,5):
    n = int(input('Digite um valor: '))
print('Fim')
#Somatoria utilizando inputs dentro de um for
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s = s + n
print(('A soma é {}'.format(s)))
print('Fim')
