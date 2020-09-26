#Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores M ou F
#Caso esteja errado, peça a digitação novamente, até ter um valor correto.
mf1 = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0] #pega apenas a primeira letra maiuscula
while mf1 not in 'MF':
    mf1 = str(input('Digite M ou F: ')).strip().upper()[0]
if mf1 == 'M':
    print('Voce é do sexo masculino')
if mf1 == 'F':
    print('Voce é do sexo feminino')
