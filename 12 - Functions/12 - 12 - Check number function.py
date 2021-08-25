#Only with information below, make a program:
#Check if its a number!
#Error shows up when the input value was not a int
#n = leiaInt('Digite um numero: ')
#print(f'Voce digitou o numero {n}')
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mDigite um numero inteiro\033[m')
        if ok:
            break
    return valor    


#Programa principal
n = leiaInt('Digite um numero: ')
print(f'Voce digitou o numero {n}')