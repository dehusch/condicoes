#Crie um programa que leia o ano de nascimento de sete pessoas
#Mostrar quantas são de maior idade e quantas de menor idade
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 4):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?: '.format(pess)))
    idade = atual - nasc
    if idade > 18:
        totmaior += 1
    elif idade < 18:
        totmenor += 1
print('São {} pessoa(s) maior de idade'.format(totmaior))
print('Sao {} pessoa(s) menor de idade'.format(totmenor))