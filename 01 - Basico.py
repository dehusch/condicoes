#PY
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:_^20}!'.format(nome)) #entre 20 caracteres é preenchido por _
a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}') #boleano, string, numero inteiro, numero quebrado
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está em minúsculas? {a.islower()}')
print(f'Está capitalizado? {a.istitle()}')
#var
print('Vamos fazer os calculos aritimeticos de 2 numeros')
n1 = int(input('Digite o primeito valor: '))
n2 = int(input('Digite o segundo valor: '))
#inicio
#calculos basicos de soma, subtração, multiplicação, divisão, divisão inteira
# resto da divisão, potencia e raiz quadrada.
a = n1 - n2
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 //n2
rd = n1 % n2
exp = n1 ** n2
ra = (n1+n2)**(1/2)
print('A subtração vale {}'.format(a), end=' e ')
print('a soma vale: {}'.format(s))
print('A Multiplicação vale: {}'.format(m))
print('A divisão vale: {}'.format(d))
print('A Divisão Inteira vale: {}'.format(di))
print('O resto da divisão: {}'.format(rd))
print('O ',n1, "elevado a potencia de ",n2,' vale: {}'.format(exp))
print('A raiz da soma dos dois numeros vale: {:.3}'.format(ra))
#
#calcula sucessor, antecessor, dobro, triplo e raiz
#
n3 = float(input('Digite um numero para calcular antecessor, sucessor, o dobro, o triplo e a raiz: '))
print('O seu antecessor é: {}'.format(n3-1))
print('E o seu sucessor é: {}'.format(n3+1))
print('O seu dobro é {}'.format(n3*2))
print('O seu triplo é {}'.format(n3*3))
print('E sua raiz é {:.3}'.format(n3**(1/2)))
#
#calcular media
#
n4 = float(input('Agora vamos calculcar uma media. Digite o primeiro valor: '))
n5 = float(input('Digite o segundo valor: '))
print('a media é: {}'.format((n4+n5)/2))
#
#Transformar metros em centimetros/milimetros
#
n6 = float(input('Digite o valor em metros para converter em centimetros e milimetros: '))
print('O valor em centimetros é: {}'.format(n6*100))
print('O valor em milimetros é: {}'.format(n6*1000))
#
#Agora essa é para o meu filho!
#Digite um valor para montar a tabuada de numeros inteiros
#
n7=int(input('Digite um numero inteiro para calcular a tabuada'))
print(n7,'x 1 =', (n7*1))
print(n7,'x 2 =', (n7*2))
print(n7,'x 3 =', (n7*3))
print(n7,'x 4 =', (n7*4))
print(n7,'x 5 =', (n7*5))
print(n7,'x 6 =', (n7*6))
print(n7,'x 7 =', (n7*7))
print(n7,'x 8 =', (n7*8))
print(n7,'x 9 =', (n7*9))
print(n7,'x 10 =', (n7*10))
#
#Conversão dolar
#
n8 = float(input('Digite o valor em Real(is) para converter em Dolar(es):'))
print(n8, 'Real(is) vale {:.3} dolar(es)'.format(n8/5.42))
#
#Pintar parede
#cada 1 litro de tinta pinta 2 metros quadrados
#
print('Vamos calcular quantos litros de tinta é necessário para pintar uma parede')
print('Sabemos que utilizamos 1 litro de tinta para cada 2 metros')
n9 = float(input('Digite a altura da parede: '))
n10 = float(input('Digite o comprimento da parede: '))
li = n9*n10
print('É necessário {:.3} litro(s) de tinta(s)'.format(li/2))
#
#Calcular porcetagem de desconto em um produto
#
print('Vamos calcular um desconto em um produto')
n11 = float(input('Digite o valor do produto: '))
n12 = float(input('Digite o desconto sem o simbolo de %'))
de = n12/100
print('O valor com desconto é {} Reais'.format(n11-(de*n11)))
#
#calcular a porcetagem de aumento de um salario
#
print('Vamos calcular uma porcentagem de aumento de salario')
n13 = float(input('Digite o salario atual: '))
n14 = float(input('Digite a porcentagem de aumento sem o simbolo de %'))
sa = n14/100
print('O valor com aumento é {} Reais'.format(n13+(sa*n13)))
print('Ola :')
#
#Calcular aluguel de Carro
#
n15 = float(input('Qual foi o KM rodado?'))
n16 = float(input('Quantos dias de aluguel?'))
print('O aluguel por dia é 60Reais e R$0.15 por KM rodado')
print('O total é {:.5f}'.format((n15*0.15)+(n16*60)))