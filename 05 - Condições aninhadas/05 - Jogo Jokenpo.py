#Crie um programa que faça o computador jogar jokenpo com você
import random
print('Vamos jogar jokenpo!')
jog1 = str(input('Escolha! Papel, Tesoura ou Pedra: '))
Papel = 'Papel'
Tesoura = 'Tesoura'
Pedra = 'Pedra'
lista = [Papel, Tesoura, Pedra]
comp = random.choice(lista)
print('O computador escolheu {}'.format(comp))
#
#Condiçoes se jogador escolher Papel
#
if jog1 == 'Papel' and comp == 'Pedra':
    print('O jogador ganhou!')
elif jog1 == 'Papel' and comp =='Tesoura':
    print('O computador ganhou!')
#
#Condicoes se jogagor escolher Pedra
#
if jog1 == 'Pedra' and comp == 'Tesoura':
    print('O jogador ganhou!')
elif jog1 == 'Pedra' and comp =='Papel':
    print('O computador ganhou!')
#
#Condicoes se jogagor escolher Tesoura
#
if jog1 == 'Tesoura' and comp == 'Papel':
    print('O jogador ganhou!')
elif jog1 == 'Tesoura' and comp =='Pedra':
    print('O computador ganhou!')
#
#Condicao de empate
#
elif jog1 == comp:
    print('Temos um empate')