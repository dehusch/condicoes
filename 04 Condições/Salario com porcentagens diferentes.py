salario = float(input('Digite o salario atual: '))
if salario <= 1250:
    novo = ((15/100)*salario)+salario
else:
    novo = ((10/100)*salario)+salario
print('O salario é {}'.format(novo))
