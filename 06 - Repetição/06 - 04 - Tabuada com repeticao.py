#Crie uma tabuada de um numero escolhido pelo usuario
#utilizando repetição (for)
num = int(input('Digite um valor: '))
for c in range(0, 11):
    print("{} x {:1} = {}".format(num, c, num*c))