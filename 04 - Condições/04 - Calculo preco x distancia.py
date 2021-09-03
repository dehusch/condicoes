#Calculo de viagem x KM rodado
#Para 200km rodado, valor e 0,50
#acima de 200km rodado, valor e 0,45
km = float(input('Digite o valor do KM rodado: '))
km50 = km * 0.50
km45 = km * 0.45
if km <= 200:
    print('O valor total será de {:.2f}'.format(km50))
else:
    print('O valor total sera de {:.2f}'.format(km45))

