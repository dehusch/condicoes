carro = int(input('Qual foi a velocidade do carro em km/h?'))
if carro > 80:
    print('Este veiculo foi multado')
    print('O custo sera de {} Reais'.format((carro - 80) * 7))
else:
    print('Este veiculo estava dentro dos limites de velocidade!')

