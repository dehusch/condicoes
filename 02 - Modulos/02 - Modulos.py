import emoji
import random
import math
from math import sqrt #somente um exemplo escolhendo a função especifica.
import pygame
num = int(input('Digite um numero:'))
raiz = math.sqrt(num)
print(f'A raide de {num}, é {raiz}') #novo formato do print
print("Arrendodar para cima o resultado é: {}".format (math.ceil(raiz)))
print("Arredondar para baixo o resultado é: {}".format (math.floor(raiz)))
#
#Importando a biblioteca Random e gerando um numero aleatorio entre 1, 10
#
num = random.randint(1, 10)
print('O numero aleatorio gerado é {}'.format (num))
#
#utilizando biblioteca de emojis
#
print(emoji.emojize(":grimacing:", use_aliases=True))
#
#Digitar numero real (quebrado) e mostrar Inteiro
#
num1 = float(input('Digite um numero com 3 casas decimais: '))
print('O numero arredondado sem casas decimais é {}'.format (math.trunc(num1)))
#
#sem o modulo math:
#
numq = float(input('Digite um numero com 3 casas depois da virgula:'))
print(f'O numero {numq} tem a parte inteira {int(numq)}')
#
#Calcular a Hipotenusa
#
num2 = float(input('Digite o valor do cateto adjacente: '))
num3 = float(input('Digite o valor do cateto oposto: '))
print('O valor da hipotenusa é: {}'.format (math.hypot(num2, num3)))
#
#Informar o valor de sen, cos, e tag. em um angulo
#
num4 = float(input('Digite um valor de um angulo: '))
sen1 = math.sin(math.radians(num4))
cos1 = math.cos(math.radians(num4))
tan1 = math.tan(math.radians(num4))
print('O valor de seno é', sen1, 'o valor de cosseno é ', cos1, "e o valor da tangente é ", tan1)
#
#Escolher um aluno pelo seu numero#
#
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
#
#Escolher a ordem de alunos
#
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação sera: \n {}'.format(lista))
#
#com numeros inteiros
#
import random
alu1 = int(3)
alu2 = int(4)
alu3 = int(6)
alu4 = int(5)
lista = [alu1, alu2, alu3, alu4]
random.shuffle(lista)
print(f'A ordem é {lista}')
#encontrando a hipotenusa
#
cato = float(input('Digite o Cateto oposto:'))
cata = float(input('Digite o Cateto adjacente:'))
hyp = ((cato**2)+(cata**2))**(1/2)
hyp1 = math.hypot(cato,cata)
print(f'A hipotenusa é {hyp}')
print(f'Usando math: {hyp1}')
#
#Encontrando seno, coseno, tangente de um angulo
#
ang = int(input('Digite um angulo:'))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O coseno é {cos}, o seno é {sen}, e a tangente é {tan}')
