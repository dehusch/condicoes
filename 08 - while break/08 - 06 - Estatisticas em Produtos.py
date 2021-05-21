#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
totalcompra = 0
produtos = 0
preco = 0
barato = " "
contprod = 0
primeiravez= 's'
while True:
    produtos = str(input("Digite o nome do produto: "))
    preco = int(input("Qual o valor do produto?: "))
    totalcompra = totalcompra + preco
    if preco > 1000:
        contprod = contprod + 1
    cont = " "
    if primeiravez == 's':
        # Definindo o nome do menor produto
        menorProduto = produtos
        # Definindo o valor do menor produto
        menorPreco = preco
        primeiravez = 'n'
    elif menorProduto > produtos:
        menorProduto = produtos
        menorPreco = preco

    while cont not in "SN":
        cont = str(input("Deseja continuar? [S/N]: ")).upper()
    if cont == "N":

        break
print(f"Total de produtos acima de 1000 é igual a: {contprod}")
print(f"Preco total: {totalcompra}")
print(f"O menor produto é: {menorProduto} ")
print(f"O valor do menor produto é: {menorPreco} ")

