#Write a scene that shows a soccer player score
#Ask the player's name and how many games played with his score
#write an option to include N players
#write an option to show players details
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
jogos = int(input('Quantas partidas jogou?: '))
for c in range(0, jogos):
    partidas.append(int(input(f'Quanto gols na partida {c+1}?: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print()
print(jogador)
print()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print()
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas!')
for i, v, in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print()
print(f'Foi um total de {jogador["total"]} gols.')