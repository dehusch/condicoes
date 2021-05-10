#Ler varios valores e informar a quantidade de valores digitados e a soma total
num = cont = soma = 0
num = int(input('Digite um valor para ser somado: '))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input('Digite um valor para ser somado: ')) # o Num repete no comeco para
#desconsiderar o 999 na soma
print(f'Voce digitou {cont} numeros e a soma deles é {soma}')

#outra forma

num = 0
contador = 0
soma = 0
num = int(input('Digite um valor [999 para cancelar]: '))
while num != 999:
  soma = soma + num
  contador = contador + 1
  num = int(input('Digite um valor [999 para cancelar]: '))
print(f'Voce digitou {contador} numeros e a soma é {soma}')