pessoas = {'nome': 'Denis', 'Idade': 37, 'Sexo': 'Masculino'}
print(pessoas['nome'])
print(pessoas['Idade'])
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items(): #Do not exist enumerate for dictionary
    print(f'{k} = {v}')
#
#Add, Changing and deleting an item
#
delpessoas = {'nome': 'Denis', 'Idade': 37, 'Sexo': 'Masculino'}
del delpessoas['Sexo']  #Deleting an item
delpessoas['nome'] = 'Joao' #Changing the item
delpessoas['Peso'] = 81.2 #add an item without append (no needed in dict)
for k, v in delpessoas.items():
    print(f'{k} = {v}')
#
#A dict inside a list
#
brasil = []
estado1 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['sigla'])
#
#Copying a dict
#
estado = dict()
estadobrasil = list()
for c in range(0, 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    estadobrasil.append(estado.copy()) #Here we make a copy from dict ESTADO
print(estadobrasil)
for e in estadobrasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
for e in estadobrasil:
    for v in e.values():
        print(v, end=' ')
    print()
