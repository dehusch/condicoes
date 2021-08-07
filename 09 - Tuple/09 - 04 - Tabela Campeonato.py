times = ("América-MG", "Athletico", "Atlético-GO", "Atlético-MG", "Bahia", "Ceará", "Chapecoense")
quantidade = int(input('Digite a quantidade de posições que deseja saber: '))

#Nesse for percorre em times a quantidade de times digitada
print('Os 5 primeiros colocados são: ')
for primeiros in range(0,quantidade):
    print( times[primeiros])

print('Os 4 últimos colocados são')
for ultimos in range(-4,0):
    print( times[ultimos])

print('Times em ordem alfabética: ')
print(sorted(times))

for posicao in range(0,time):
    print( times[primeiros])


