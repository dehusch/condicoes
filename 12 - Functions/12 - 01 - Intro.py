#
#Def simples
#
def lin():
    print('-' * 30)


#programa principal
lin()
print('Python')
lin()

#
#Def simples
#

def soma(a, b):
    s = a + b
    print(s)


#Programa Principal
soma(3, 2)
soma(4, 3)
soma(2, 11)
soma(a=2, b=3)
soma(b=3, a=20)

#
#Def simples
#
def titulo(txt):
    print("-" * 30)
    print(txt)
    print("-" * 30)

#Programa principal
titulo('             Python           ')

#
#def simples
#
def somaAB(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

#Programa Principal
somaAB(4, 3)
somaAB(a=11, b=32)
somaAB(b=10, a=20)

#
#def tuplas
#
def contador(* num): #quando nao sei a qtde de numeros totais
    print(num)

#Programa principal
contador(2, 1, 4)
contador(4, 2, 5, 7)

#
#def Tuplas for (contando os numeros fora da tupla)
#
def cont(* num): #quando nao sei a qtde de numeros totais
    for valor in num:
        print(f'{valor} ', end='')
    print()
    tam = len(num)
    print(f'Os valores sao {num} e sao ao todo {tam}')
    print('FIM!')


cont(2, 1, 4)
cont(4, 2, 5, 7)

#
#Def lista dobrando os valores
#
def dobra(lst): #uma funcao para dobrar os valores de uma lista
    pos = 0
    while pos < len(lst):
        lst[pos] = lst[pos] * 2
        pos = pos + 1

#programa principal
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# 
#Def soma for
#

def somafor(* val):
    s = 0
    for num in val:
        s = s + num
    print(f'Somando os valores {val} temos {s}')


#programa principal
somafor(5, 2)
somafor(2, 7, 2)
