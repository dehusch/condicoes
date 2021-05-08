#sequencia de fibonacci
#sequencia de fibonacci é 0 - 1 -1 - 2 - 3 - 5 - 8
#0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 3 + 2 = 5, 5 + 3 = 8
#To assume the next value, we have to change the t1 and t2 position
#cont = 3 'cause for 3 results it's not necessary the loop
n = int(input('Quantas sequencias você quer?: '))
t1 = 0
t2 = 1
print(f'{t1} > {t2}', end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' > {t3}', end=' ')
    t1 = t2 #t1 assumindo o valor de t2
    t2 = t3 #t2 assumindo o valor de t3
    cont = cont + 1
print('Fim')