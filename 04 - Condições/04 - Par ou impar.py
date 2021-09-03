#Descobrir se um numero é par ou impar
#Para ter um resultado 0 ou 1 em um numero escolhido, basta utilizar a regra de operadores
#Todo resto de divisão (simbolo %) pode ser ou 0 ou 1.
#Com isso conseguimos identificar se o numero é par ou impar.
numero = int(input('Me diga um numero: '))
numero = numero % 2 # Resto da divisão
if numero == 1:
    print('O numero é impar')
else:
    print('O numero é par')