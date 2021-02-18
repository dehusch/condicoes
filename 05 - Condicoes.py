tempo = int(input('Quantos anos tem seu carro:'))
if tempo <=3 :
    print('Carro novo')
else:
    print('Carro Velho')
print('FIM')
#
# SIMPLIFICADO para situações simples
#
tempo = int(input('Quantos anos tem seu carro:'))
print('carro novo' if tempo<=3 else 'carro velho')
print('Fim')
#
#Formato novo
#
nome = input('Qual seu nome?: ')
if nome == 'Denis':
    print(f'Ola {nome}, tudo bem?')
else:
    print(f'Você não é o Denis')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2
if media >= 6.0:
    print('Você foi aprovado')
else:
    print(f'É uma pena {nome}, você foi reprovado')
print(f'Sua nota foi: {media}')
#
#Formato antigo
#
nome = str(input('Digite seu nome: '))
if nome == 'Denis':
    print('Olá Denis, Seja bem vindo!')
else:
    print('Olá {}, voce não é o Denis!'.format(nome))
nota = float(input('Digite sua nota: '))
if nota >= 5:
    print('Voce foi aprovado')
else:
    print('Voce foi reprovado')

