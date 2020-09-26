#Crie um programa que calcule a soma de todos numeros impares multiplos de 3
#em um intervalo de 0 a 500
#Dica é saber se o numero é divisivel por 3, se sim = 0 (eu acho)
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = c + s
        cont = cont + 1
print('A soma de {} valores encontrados é {}'.format(cont, s))
