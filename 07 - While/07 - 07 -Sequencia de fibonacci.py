#sequencia de fibonacci
#sequencia de fibonacci é 0 - 1 -1 - 2 - 3 - 5 - 8
#0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 3 + 2 = 5, 5 + 3 = 8
n = int(input('Quantas sequencias você quer?: '))
t1 = 0
t2 = 1
print(f'{t1} > {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' > {t3}', end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('Fim')