#create a square calc terrain with function
def area():
    area = largura * comprimento
    print(f'A area do terreno {largura}x{comprimento} é de {area}')


#Programa principal
largura = float(input('LARGURA: '))
comprimento = float(input('COMPRIMENTO: '))
area()