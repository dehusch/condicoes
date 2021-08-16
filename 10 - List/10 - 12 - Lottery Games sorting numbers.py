#Create a loterry generator asking how many games will be
#the numbers must be between 1 and 60 in crescent sort.
#the program follows the rules that should be done a list inside another list.
from random import randint
lista = list()
games = list()
quant = int(input('Quantos jogos?'))
total = 1
while total <= quant:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count = count + 1
        if count >= 6:
            break
    lista.sort()
    games.append(lista[:])
    lista.clear()
    total = total + 1
for i, l in enumerate(games):
    print(f'Jogo {i+1}: {l}')
print('FIM')