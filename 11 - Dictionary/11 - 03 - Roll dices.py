#Create a program that pick a random dice number for a player
#organize this number in a dictionary
#Organize the dictionary according to player number
from random import randint
from time import sleep
from operator import itemgetter
players = {'Jogador 1' : randint(0, 6),
            'Jogador 2' : randint(0, 6),
            'Jogador 3' : randint(0, 6)}
placar = list()
for k, v in players.items():
    print(f'{k} jogou {v}')
    sleep(1)
placar = sorted(players.items(), key=itemgetter(1), reverse=True) #the result is a list
print(placar)
for i, v in enumerate(placar): #If it is a list, we can use enumerate
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('FIM')
