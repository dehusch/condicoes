#Counting to 10 one by one
#Counting to 10 two by two
#Counting to unknown number by unknown steps
from time import sleep
def contador(i, f, p): #INICIO, FIM, PASSO
    if p < 0:   #aqui é que define o passo personalizado
        p = p * -1
    if p ==0:
        p = 1
    print(f'Contagem de {i}, até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont -= p
        print('Fim!')


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print()
ini = int(input('Digite o inicio: '))
fim = int(input('Digite o fim:'))
pas = int(input('Digite o passo: '))
contador(ini, fim, pas)














#
#My way
#
print()
def count10():
    for c in range(0, 10):
        c = c + 1
        print(c, end='')
    print(' Fim!')


print(count10())

def count10by2():
    for c in range(5, 0, -1):
        c = c * 2
        print(c, end='')
    print(' Fim!')


print(count10by2())
