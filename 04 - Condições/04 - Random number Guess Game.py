#Jogo para adivinhar um numero aleatorio de 0 a 5
import random
num = random.randint(1, 5)
jogador = int(input('Em que numero eu pensei?'))
print('O numero aleatorio gerado é {}'.format (num))
if num == jogador:
    print('Parabens, voce acertou')
else:
    print('voce errou')
