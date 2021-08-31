def linha(tam=42):
    return '~' * tam

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuario preferiu nao digitar um numero.\033[m')
            return 0
        else:
            return n


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c = c + 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc