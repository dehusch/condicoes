#Crie um programa que atraves de 3 medidas informas, o programa identifica se é ou não possivel fazer
#um triangulo, e se for possivel, qual tipo de triangulo é:
#triangulo equilatero: Todos lados iguais
#Triangulo Isoceles: Dois lados iguais
#Triangulo Escaleno: Todos lados diferentes.
print('=-='*30)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
print('=-='*30)
print('Analisador de triangulos')
print('=-='*30)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triangulo escaleno!')
else:
    print('Os segumentos acima não podem formar um triangulo')
if r1 == r2 == r3:
    print('Os seguimentos acima podem formar um triangulo equilatero')
elif r1 == r2 or r2 == r3 or r3 == r1:
    print('Os seguimentos acima podem formar um triangulo isoceles')
