#Analide de dados
#quantos acima de 18 anos
#quantas mulheres acimda de 20 anos
#quanto homes
contidade = 0
contsexom = 0
contsexof = 0
while True:
    idade = int(input("Qual a idade: "))
    sexo = str(input("Qual é o sexo [M/F]: ")).upper()
    cont = str(input("Deseja continuar? [S/N]: ")).upper()
    if cont == "S":
        if idade >= 18:
            contidade = contidade + 1
        if sexo == "M":
            contsexom = contsexom + 1
        if sexo == "F":
            if idade > 20:
                contsexof = contsexof + 1
    else:
        print(f"São {contidade} pessoa(as) maior de 18 anos")
        print(f"São {contsexof} Mulher(es) maior de 20 anos")
        print(f"São {contsexom} Homen(es)")
        break
print("FIM")

#
#OUTRA FORMA
#
# copy from https://gist.github.com/EduardoLimas
#
#Neste caso é utilizado o while "variavel" not in "String"
#

maioridade = mulheres = homens = mulheresmenosvinte = 0
while True:
    print('--' * 20)
    print('Vamos preencher os dados')
    print('--' * 20)
    idade = int(input('Insira a idade: '))
    if idade >= 18:
        maioridade +=1
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Insira o sexo(M/F): ')).lower().strip()[0]
    if sexo in 'm':
        homens += 1
    elif sexo in 'f':
        mulheres += 1
    if sexo in 'f' and idade < 20:
        mulheresmenosvinte += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar?(S/N) ')).strip().lower()[0]
    if continuar in 'n':
        break
print(f'''{maioridade} pessoas têm mais de 18 anos.
Foram cadastrados {homens} homens.
{mulheresmenosvinte} mulheres têm menos de 20 anos.''')