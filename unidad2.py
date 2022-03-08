#manejo de importaciones y uso
    #import random
    #import os, sys
    #from math import factorial

#uso de modulos
import random
print(random.randint(10,50)) 

#randint nos da un número aletaorio entre el 0 y 1
comienza = random.randint(0,1) #variable
if comienza == 0:
    print('Comienza el jugador')
else:
    print('Comienza el PC')

#Ejemplo randit
x=1
n2=0
while (x<=6):
    numero = random.randint(1,6)
    print("El número obtenido es: ", numero)
    if numero == 2:
        n2 = n2+1
    x = x+1
print("El número de veces que salió 2 son", n2)

#Número aleatorio lanzamiento del dado
numero = random.randint(1,6)
print("El número obtenido es: ",numero)

#randrange nos da un número aleatorio no mayor al 10 o 100
print(random.randrange(10))
print(random.randrange(100))

for i in range(10):
    print(random.randrange(5, 27, 4)) #inicio, termina, intervalo de brinco

from math import factorial
print(factorial(5))

#Ejemplo de uso de random

for i in range(1,16):
    print(i,"=", random.random())



for i in range(5):
    print(random.uniform(100,200))