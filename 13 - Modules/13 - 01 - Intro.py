def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x')
        f = f * c
    return f


print(fatorial(5, show=False)) #Se definir false não aparece o calculo
help(fatorial)