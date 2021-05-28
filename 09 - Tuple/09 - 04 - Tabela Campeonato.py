time = ("América-MG", "Athletico", "Atlético-GO", "Atlético-MG", "Bahia", "Ceará", "Chapecoense")

'''os ultimos 4 colocados
ordem alfabética
em que posicao está x time
'''

#quantidade = int(input('Digite a quantidade de posições que deseja saber: '))
quantidade = 5
#Nesse for percorre em times a quantidade de times digitada
for primeiros in range(0,quantidade):
    print( time[primeiros])
    print(' ----------------------')

for ultimos in range(0,len(time)):
    print( time[(len(time))- ultimos])


