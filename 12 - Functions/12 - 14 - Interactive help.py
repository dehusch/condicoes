#Busca a ajuda referente a um comando!
#
def ajuda(com):
    help(com)


#Programa principal
comando = ''
while True:
    comando = str(input('Funcao ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)