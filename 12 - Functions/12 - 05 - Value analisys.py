def value(*num):
    print('-' * 30)
    print(f'{num}! Foram informados {len(num)} numeros')
    maior = sorted(num)
    print(f'O maior valor é {(maior[-1])}')



#Programa principal
value(1, 2, 3)
value(7, 8, 100, 5, 33)
value(6)

#
#
#
#Another way
#
#
#
#
from time import sleep

def maior(*num):
    cont = maior = 0
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont= cont + 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informado foi {maior}')


#programa principal
maior(5, 7, 8, 9, 10, 300, 1)
maior()