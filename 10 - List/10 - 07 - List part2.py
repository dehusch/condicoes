teste = list()
teste.append('Denis')
teste.append(37)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = '22'
galera.append(teste[:])
print(galera)
#
#
#
pessoas = [['Joao', 11], ['Maria', 22], ['Ana', 33], ['Jose', 44]]
print(pessoas)
print(pessoas[0])
print(pessoas[0][0])
print(pessoas[2])
print(pessoas[2][1])
for p in pessoas:   #make a list of pessoas
    print(p)
for p in pessoas:   #Print names
    print(p[0])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')
#
#
#
people = list()
data = list()
totmaior = totmenor = 0
for c in range(0, 3):
    data.append(str(input('Nome: ')))
    data.append((int(input('Idade: '))))
    people.append(data[:])      #copy from data list
    data.clear()                #delete data list
print(people)

for p in people:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior = totmaior + 1
    else:
        print(f'{p[0]} é menor de idade')
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')