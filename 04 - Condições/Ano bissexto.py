from datetime import date
ano = int(input('Qual é o ano que deseja saber se é bissexto? Digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year #importa da biblioteca o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # dividido por 4 e 400 o resto da divisão tem que dar 0
    print('O ano {} é  bissexto!'.format(ano))#Quando dividido por 100 o resto da divisao tem que ser diferente de 0 (!=)
else:
    print ('O ano {} não é bissexto'.format(ano))
