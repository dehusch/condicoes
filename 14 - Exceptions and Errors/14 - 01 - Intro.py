#print(x) #erro semantico X não definido
#Exception
#Uma exceção    #NameError
                #ValueError
                #ZeroDivisionError
                #TypeError
                #IndexError or KeyError
                #ModuleNotFoundError
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Existe problemas com o tipo de dados digitado')
except ZeroDivisionError:
    print('Nao existe divisao por 0')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('FIM!!!!')