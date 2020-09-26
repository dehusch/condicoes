#Ler varios valores e informar a quantidade de valores digitados e a soma total
num = cont = soma = 0
num = int(input('Digite um valor para ser somado: '))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input('Digite um valor para ser somado: ')) # o Num repete no comeco para
#desconsiderar o 999 na soma
print(f'Voce digitou {cont} numeros e a soma deles é {soma}')