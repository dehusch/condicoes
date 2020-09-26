#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade
#Se ele ainda vai se alista ao serviço militar
#Se é o ano que ele vai se alistar
#Se já passou do tempo de alistamento
#Mostrar tambem o tempo que falta/passou do alistamento
#Dica, pegar o ano do sistema
import datetime
from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento:'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade > 18:
    idade = atual - (nasc + 18)
    print('Ja passsou {} anos do tempo de alistamento'.format(idade))
elif idade < 18:
    idade = (nasc + 18) - atual
    print('Ainda faltam {} ano(s) para se alistar'.format(idade))
else:
    print('Este é o ano de alistamento')
