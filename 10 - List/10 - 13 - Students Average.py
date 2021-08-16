#Create a list for students with two scores
#Shows at the end the Full score avarage and allows the user to choose a student to see his scores.
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar?[S/N]: '))
    if resp in 'Nn':
        break
print(f'{"No.":<4}{"Nome":<10}{"MEDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Qual aluno deseja ver? [999 para cancelar]'))
    if opc == 999:
        print('FIM')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('OBRIGADO!')