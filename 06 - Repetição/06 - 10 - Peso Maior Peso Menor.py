#Crie um programa que leia o peso de 5 pessoas
#Mostrar quem é o maior peso e quem é o menor peso:
maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))