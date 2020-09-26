nome = str(input('Qual é o seu nome? '))
if nome == 'Denis':
    print('Herzlich Wilkommen')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome e bem comum! Seja bem vindo!')
elif nome in 'Claudia Ana Juliana':
    print('Este é um nome feminino bem comum!')
else:
    print('Seja bem vindo')
print('Tenha um bom dia {}'.format(nome))

#Pode existir 1 if e varios elif's
#Else pode ou não existir, mas ELSE só pode ter uma vez