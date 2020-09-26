#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario.
#Caso exceda o valor, o emprestimo sera negado.
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
sal30 = (30 / 100)
salario = (sal30*salario)
anos = int(input('Digite em quantos anos deseja pagar: '))
anos = anos * 12
anca = casa / anos
print('30% de salario é {}'.format(salario))
print('O valor mensal será de {:.3f}'.format(anca))
if anca < salario:
    print('O emprestimo foi aprovado')
else:
    print('O valor da mensalidade excede 30% de seu salario')
