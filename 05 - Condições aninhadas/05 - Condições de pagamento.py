#Crie um programa que calcule o preço de um produto considerando seu preço e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartao: 5% de desconto
# em até 2x no cartão: preço normal
# em 3x ou mais no cartão: 20% de juros:
preco = float(input('Qual o valor do produto? '))
cond = str(input('Qual a forma de pagamento? Cheque, Dinheiro ou Cartao? '))
descd = 10/100
descc = 5/100
jurc = 20/100
#
#Se escolher dinheiro ou cheque
#
if cond == 'Dinheiro' or cond == 'Cheque':
    preco = preco-(preco*descd)
    print('O valor total é {}'.format(preco))
#
#Se escolher cartao
#
elif cond == 'Cartao':
    cond2 = str(input('Vista ou Parcelado? '))
    if cond2 == 'Vista':
        preco = preco-(preco*descc)
        print('O valor total sera {}'.format(preco))
    elif cond2 == 'Parcelado':
        cond3 = str(input('2x ou 3x? '))
        if cond3 == '2x':
            print('O preço total sera {}'.format(preco))
        else:
            preco = preco+(preco*jurc)
            print('O preco total sera {}'.format(preco))
