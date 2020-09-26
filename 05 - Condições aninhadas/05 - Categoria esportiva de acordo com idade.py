#Escreva um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo
#com a idade:
#Ate 9 anos: Mirim
#Ate 14 anos: Infantil
#Ate 19 anos: Junior
#Ate 25 anos: Senior
#Acima: Master7
idade = int(input('Digite sua idade:'))
if idade <= 9:
    print('Sua categoria é mirim')
elif 10 <= idade <= 14:
    print('Sua categoria é Infantil')
elif 15 <= idade <= 19:
    print('Sua categoria é Junior')
elif 20 <= idade <= 25:
    print('Sua categoria é Senior')
else:
    print('Sua categoria é Master')