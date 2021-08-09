num = [2, 5, 9, 1]
number = [2, 4, 5, 6, 7, 8, 1]
numbers = [2, 5, 19, 3, 6, 8, 11, 4, 1, 6]
num[2] = 3 #substitui o numero
num.append(9) #adiciona o numero 9 no fim da lista
num.sort()  #organiza a lista em ordem crescente
number.insert(2, 11) # adiciona o item "11" na posicao 2
number.pop(3) #elimina o item na posicao 3
number.remove(4) #procura o primeiro numero 4 da lista e remove. Ele da erro se não achar o numero
numbers.sort(reverse=True) # organiza a lista em ordem decrescente
print(num)
print(number)
print(numbers)
print(f'Minha lista numbers tem {len(numbers)} elementos')
#para tentar remover um item de uma lista, deve criar uma condição.
if 12 in number:
    number.remove(12)
else:
    print(f'Não achei o numero 12 na lista {number}')
#
#Para criar uma lista vazia
#
emptymodel1 = list() #pode criar um lista vazia apenas com []
emptymodel2 = [] #pode criar uma lista vazia com o comando list()
emptymodel1.append(1)
emptymodel1.append(2)
emptymodel1.append(9)
for v in emptymodel1:
    print(f'{v}...')
for c, v, in enumerate(emptymodel1):
    print(f'Para a posicao {c}, o valor é {v}')
#
#Adicionar uma lista por input
#
for cont in range(0, 2):
    emptymodel2.append(int(input('Digite um valor: ')))
for v in emptymodel2:
    print(f'{v}...')
for c, v, in enumerate(emptymodel2):
    print(f'Para a posicao {c}, o valor é {v}')
#
#Duplicar listas com variaveis
#
a = num #aqui eu falo que a variavel "a" é igual minha lista num
a[2] = 3 #aqui eu altero as duas listas pois elas criam uma ligacao
print(a)
print(num)
#
#Criar um copia de uma lista com uma variavel
#
b = number[:] #com esse comando eu crio uma copia da lista number
b[2] = 3 #aqui eu só altero o item 2 da lista B que foi copiada, e a lista number não muda
print(b)
print(number)