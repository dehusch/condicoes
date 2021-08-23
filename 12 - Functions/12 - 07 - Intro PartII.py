#Interactive Help
# help(print) #mostra a ajuda do comando print
# print(print.__doc__) #mostra a ajuda com mais detalhes
def contador(i, f, p):
    """
        Faz uma contagem e mostra na tela
        i = inicio da contagem
        f = fim da contagem
        p = passo da contagem
        return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c = c + p
    print('FIM')

# help(contador) #O comentario adicionado acima aparece na tela
contador(2, 10, 2)
#
#
#
#
#
#PARAMETRO OPCIONAL
def somar(a, b, c=0): #Pode definir um parametro opcional
    """
        Soma os itens A, B, C
        A = Primeiro valor
        B = Segundo Valor
        C = Terceiro Valor
        Caso o C não for preenchido, o valor sera 0.
    """
    s = a + b + c
    print(f'A soma é {s}')


somar(2, 3, 5)
somar(2, 3) #O param C não foi definido, então será 0
#
#
#
#
#
#ESCOPO DE VARIAVEIS
def teste():
    global n2   #substituido o n2 global (era 30, virou 75)
    x = 8
    n1 = 10 #No principal, n1 = 20
    n2 = 75 #Com o comando global n2, o n2 no programa principal sera substituido.
    print(f'Na funcao teste(), n vale {n}')
    print(f'Na funcao teste(), n1 vale {n1}')
    print(f'Na funcao teste(), n2 vale {n2}')
    print(f'Na funcao teste(), x vale {x}')


#PROGRAMA PRINCIPAL
n = 2
n1 = 20
n2 = 30
print(f'No programa principal, n vale {n}')
print(f'No programa principal, n1 vale {n1}')
print(f'No programa principal, n2 vale {n2}') #n2 foi substituido por n2 de teste()
teste()
#o N é uma variavel global
#O X só existe dentro da funcao teste()
#
#
#
#
#
#
#RETORNO DE VALORES
def somar(a, b, c=0): #Pode definir um parametro opcional
    s = a + b + c
    return s

r1 = somar(2, 4)
r2 = somar(10, 10, 10)
resp = somar(2, 3, 5)
print(f'A soma é {somar(2, 7, 9)}')
print(f'O valor de r1 é {r1}')
print(f'O valor de r2 é {r2}')
#
#
#
#
#
#
#
#Fatorial de um numero
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f = f * c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
#
#
#
#
#
#
#
#Par Impar
def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('PAR')
else:
    print('IMPAR')
