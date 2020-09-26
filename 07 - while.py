#Para quando não se sabe o limite de uma situação utiliza-se o while
#O while pode ser utilizado também quando se sabe o limite
#Por exemplo
for c in range(1, 10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c = c + 1
print('fim')

#Quando o limite é desconhecido

c = 0
while c != 1:   #Aqui ele fica repetindo ate ser digitado 1
    c = int(input('Digite um valor: '))
print('Fim')

#Quando o limite é desconhecido, mas definimos quando queremos parar.

c = 0
r = 'S'
while c != 1:   #Aqui ele fica repetindo ate ser digitado 1
    c = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper() #Aqui ele para se digitar N
print('Fim')

#Inserir varios valores e analisar se é par ou impar:
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Voce digitou {} numero(s) par(es) e {} numero(s) impar(es)'. format(par, impar))
