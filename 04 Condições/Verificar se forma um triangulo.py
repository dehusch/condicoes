print('=-='*30)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
print('=-='*30)
print('Analisador de triangulos')
print('=-='*30)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triangulo!')
else:
    print('Os segumentos acima não podem formar um triangulo')

