#Crie um programa de contagem regressiva de 10 a 0 com pausa de 1 segundo
#usar biblioteca para esperar tempo
#usar emoji de fogos estourando
import time
import emoji
for c in range(10, -1, -1):
    print('{} '.format(c))
    time.sleep(1)
print(emoji.emojize('Feliz ano novo!! :tada: :fireworks:', use_aliases=True))

