#Crie um programa que leia o primeiro termo de um PA (Progressao aritimetica)
#e mostre os 10 primeiros termos dessa progressão
ini = int(input('Digite o razao da PA: '))
r = int(input('Digite a inicio da PA: '))
termo = r
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ', end='')
        termo = termo + ini
        cont = cont + 1
    print('')
    mais = int(input('Quantos PA você quer ver a mais?'))
print(f'Foram feitas um total de {total} progressões')
print('Fim')

