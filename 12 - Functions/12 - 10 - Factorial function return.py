#Fatorial de um numero
#utilizar a opcao show para mostrar a conta
def fatorial(n, show=False):
    '''
    A funcao calcula um fatorial de um numero
    :param n: O numero a ser calculado
    :param show: (opcional) Mosta ou não o calculo
    :return: O valor do fatorial de um numero n
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x')
        f = f * c
    return f


print(fatorial(5, show=True)) #Se definir false não aparece o calculo
