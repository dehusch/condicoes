#Ler altura e sexo da pessoa e informa o peso ideal
sex1 = str(input('Digite o seu sexo [M/F]: ')).upper()
alt1 = float(input('Digite a sua altura em metros: '))
masc = (72.7 * alt1) - 58
fem = (62.1 * alt1) - 44.7
if sex1 == 'M':
    print(f'Seu sexo é masculino e seu peso ideal é: {masc}')
else:
    print(f'Seu sexo é feminino e seu peso ideal é: {fem}')
