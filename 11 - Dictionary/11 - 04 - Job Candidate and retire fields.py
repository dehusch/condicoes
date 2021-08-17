#Create a programm including in a dict that reads:
#name, birth year, Job Document Number, age
#if JDN is not 0, added to dict employer dating and salary
#calculate with how many years will be retired.
from datetime import datetime
cadastro = dict()
while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['nasc'] = int(input('Ano Nascimento: '))
    cadastro['carteira'] = int(input('Carteira'))
    resp = str(input('Quer continuar?[S/N]: '))
    idade = 2021 - cadastro['nasc']
    if resp in 'Nn':
        print(f'Voce tem {idade} anos')
        break
    elif cadastro['carteira'] > 0:
        cadastro['contratacao'] = int(input('Qual ano de contratação?: '))
        cadastro['salario'] = str(input('Qual o seu salario:'))
        aposent = cadastro['contratacao'] + 35
        print(f'Voce vai se aposentar em {aposent}')
        break
print(cadastro)
#
#Otherway
#
dados =  dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 para não): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Salario: '))
    dados ['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
for k, v, in dados.items():
    print(f' - {k} tem o valor {v}')
print('FIM')
