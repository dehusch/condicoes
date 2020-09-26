#Jogo para adivinhar um numero aleatorio de 0 a 5
#com a opção do jogador tentar até acertar
import random
num = random.randint(1, 5)
palpites = 1
jogador = int(input('Em que numero eu pensei?: '))
while num != jogador:
    jogador = int(input('Voce errou, tente novamente: '))
    palpites = palpites + 1
    if num < jogador:
        print('É um numero menor')
    elif num > jogador:
        print('É um numero maior!')
print('Parabens, você acertou!')
print(f'Voce acentrou com {palpites} palpites')