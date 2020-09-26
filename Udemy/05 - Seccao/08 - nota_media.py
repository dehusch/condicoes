#Limitar o usuario a digitar entre 0
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
if nota1 == 0 <= 10 and nota2 == 0 <= 10:
    media = (nota1 + nota2) / 2
    print(media)
else:
    print('O numero digitado não esta entre 0 e 10.')