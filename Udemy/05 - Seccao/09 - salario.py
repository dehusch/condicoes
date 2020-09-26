sal1 = float(input('Digite o valor do salario: '))
emp1 = float(input('Digite o valor da prestacao: '))
porcen = 20/100
aprov = sal1-(porcen*sal1)
if emp1 > aprov:
    print('O emprestimo não pode ser concedido')
else:
    print('O emprestimo foi aprovado')

