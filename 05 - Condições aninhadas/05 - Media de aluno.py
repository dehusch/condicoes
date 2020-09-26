#Crie um programa que leia duas notas de um aluno e calcule sua media, mostando uma mensagem
#no final, de acordo com a media atingida;
#Media abaixo de 5: Reprovado
#Media entre 5 e 6.9: Recuperação
#Media 7 ou superior: Aprovado
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print("A media do aluno é {}".format(media))
if media < 5:
    print('Aluno esta reprovado!')
elif 5 <= media < 6.9:
    print('O aluno esta de recuperacao!')
else:
    print('O aluno esta aprovado!')