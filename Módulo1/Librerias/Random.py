#Libreria Random

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


baraja=[1,2,3,4,5,7,10]
print(bajara)
for i in range(3):
    random.shuffle(baraja) ##shuffle nos da de forma aleatora nuestra lista
    print(baraja)

baraja=[1,2,3,4,5,7,10]
random.sample(baraja,5) #nos escoge (en este caso) 5 numeros aleatorios de la lista

#Retorna un objeto capturando el estado interno del generador
random.seed(0,2)
random.setstate(random.gestate())
random.getstate()

random.triangular()

for i in range(1,16):
    print(i,"=", random.random())

#Como dar formato (quitar decimales)
for i in range(5):
    print(random.uniform(100,200))

print("{:.4f}".format(random.uniform(100,200))) #el 4 indica que son 4 decimales
print("{:.2f}".format(random.random()))
print(round(random.random(),2))

#Random choice nos da textualmente una opción
frutas = ['peras','manzanas','plátanos']
for i in range(3):
    print(random.choice(frutas))