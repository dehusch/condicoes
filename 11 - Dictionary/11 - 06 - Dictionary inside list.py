#Create a record file for people
#reads name, sex, age of N people
#record it on a dict inside a list
#Shows how many people recorded, age avarage, a woman list and shows the age above the avarage
galera = list()
pessoa = dict()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Escolha M ou F')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print(galera)
