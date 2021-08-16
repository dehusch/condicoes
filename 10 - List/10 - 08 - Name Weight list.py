#Read name and weight and shows in a list
#How many people was added?
#What is the top highest heavyweight people?
#What is the top highest lightweight people?
people = list()
peopletemp = list()
maior = menor = 0
while True:
    peopletemp.append(str(input('Nome: ')))
    peopletemp.append(float(input('peso: ')))
    if len(people) == 0:
        maior = menor = peopletemp[1]
    else:
        if peopletemp[1] > maior:
            maior = peopletemp[1]
        if peopletemp[1] < menor:
            menor = peopletemp[1]
    people.append(peopletemp[:])
    peopletemp.clear()
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print(people)
print(f'Foram digitados {len(people)} nomes')
print(f'O maior peso foi de {maior}Kg', end=' ')
for p in people:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {menor}Kg', end=' ')
for p in people:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()
print('FIM')
