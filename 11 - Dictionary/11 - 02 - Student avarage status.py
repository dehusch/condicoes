#Create a program that must input the student name and avarage
#Include the current situation  if approve or not in a dict.
#Avarage = 7
#Show all contents in the end.
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))
print(f'O aluno é {aluno["nome"]}')
print(f'A media é  {aluno["media"]}')
if aluno['media'] >= 7:
    print(f'O {aluno["nome"]} foi aprovado')
else:
    print(f'O {aluno["nome"]} foi reprovado')
print('FIM')

