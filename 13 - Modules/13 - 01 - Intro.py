#I can use external py files as a module library.
#importing as an existing library in python...
#We can do it under two ways...
import uteis #Here I just set the library, it's the recomended way
from uteis import triplo #Here we can have some trouble as arguents.
import pacote

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num) #quando não especifico no import
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}') #quando não especifico no import
print(f'O triplo de {num} é {triplo(num)}') #quando especifico no import

#
#PACOTES (PACKAGE)
#For a structural sorted programming, for huge coding
#lines, we can split it in packages

print(f'O Quadruplo de {num} é {numeros.quadruplo(num)}') #AQUI VEM DO PACOTE
