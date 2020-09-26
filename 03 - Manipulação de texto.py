#022: Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.
#
nome1 = str(input('Qual o seu nome completo? '))
print('O nome em maiúsculo fica: {}'.format(nome1.upper()))
print('O nome em minúsculo fica: {}'.format(nome1.lower()))
e = nome1.count(' ')
print('O nome tem {} letras ao total'.format(len(nome1) - e))
list = nome1.split()
print('O primeiro nome tem {} letras'.format(len(list[0])))
#
#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#
print('Exercício 23 ')
n1=str(input('Digite um número de 0 a 9999: '))
n1=(4*'0')+n1
print('Unidade: {}'.format(n1[-1]))
print('Dezena: {}'.format(n1[-2]))
print('Centena: {}'.format(n1[-3]))
print('Milhar: {}'.format(n1[-4]))
#
#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
#
n=input('O nome da sua cidade:')
dividido=n.split()
t=dividido[0].title()
c='Santo'in t
print('Sua cidade começa com Santo: {}'.format(c))
#
#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#
nome = input('Digite seu nome: ')
if nome.find('silva') >= 0:
  print('seu nome tem silva')
else:
  print('seu nome nao tem silva')
#
#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
#
p = str(input('Digite uma frase: '))
p = p.lower()
ca = p.count('a')
fa = p.find('a')
fl = p.rfind('a')
print(f'Sua frase tem {ca} vezes a letra A.')
print(f'Sua frase tem pela primeira a letra A na posicao {fa}')
print(f'Sua frase tem pela ultima vez a palavra A na posicao {fl}')
#
#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#
nome2 = str(input('Digite seu nome completo: '))
first = nome2.split()
last = len(first)-1
print('Olá, {} {}. Seja bem-vindo(a)'.format(first[0], first[last]))