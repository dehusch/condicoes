#Crie um programa que leia o primeiro termo de um PA (Progressao aritimetica)
#e mostre os 10 primeiros termos dessa progressão
ini = float(input('Digite o razao da PA: '))
r = float(input('Digite a inicio da PA: '))
for c in range(0, 10,):
    r = r + ini
    print('{}'.format(r))

