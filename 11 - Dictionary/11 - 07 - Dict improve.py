#Write a scene that shows a soccer player score
#Ask the player's name and how many games played with his score
#write an option to include N players
#write an option to show players details
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input('Quantas partidas jogou?: '))
    partidas.clear()
    for c in range(0, jogos):
        partidas.append(int(input(f'Quanto gols na partida {c+1}?: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('S ou N')
    if resp == "N":
        break
print()
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()
while True:
    busca = int(input('Mostrar dados de qual jogador?: (999) para cancelar'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Codigo {busca} não existe')
    else:
        print(f'Detalhes do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print()
print('FIM')
