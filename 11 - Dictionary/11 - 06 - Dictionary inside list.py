#Create a record file for people
#reads name, sex, age of N people
#record it on a dict inside a list
#Shows how many people recorded, age avarage, a woman list and shows the age above the avarage
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Escolha M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
media = soma / len(galera)
print(galera)
print(f'Pessoas cadastradas: {len(galera)}')
print(f'A media de idade é {media:5.2f} anos')
print(f'As mulheres foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('As pessoas acima da media:')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('FIM')
