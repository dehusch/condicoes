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