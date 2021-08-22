#create a square calc terrain with function
def area():
    area = largura * comprimento
    print(f'A area do terreno {largura}x{comprimento} é de {area}')


#Programa principal
largura = float(input('LARGURA: '))
comprimento = float(input('COMPRIMENTO: '))
area()
#
#Another way
#
def terreno(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m2.')


l = float(input('LARGURA: '))
c = float(input('COMPRIMENTO: '))
terreno()