#EJERCICIOS MATH
#seno de pi/2, pi es la entidad
import math
print(math.sin(math.pi/2))

from math import sin, pi #importación selectiva
print(sin(pi/2)) #useo de entidades importadas y obtiene resutado

#ambas namespaces no se afectan
def sin(x): #redefinen pi y sin (reemplazan)
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
pi = 3.14
print(sin(pi/2))
print(math.sin(math.pi/2))

#cambio de palabra
import math as m #le ponemos un alias a math
print(m.sin(m.pi/2))
#ejemplo 2 de importar con alias
from math import pi as PI, sin as sine
print(sine(PI/2))

#ceil(x) → devuelve el entero más pequeño mayor o igual que x.
#floor(x) → el entero más grande menor o igual que x.
#trunc(x) → el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).

#Módulos útiles
from math import pi, radians, degrees, sin, cos, tan, asin
ad = 90
ar = radians(ad)
ad = degrees(ar)
print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

from math import e, exp, log #Euler, exponente, logaritmo
print(pow(e, 1) == exp(log(e))) #e = constante aproximada del número Euler
print(pow(2, 2) == exp(2 * log(2))) #pow encuentra el valor de (x, y) = x^y
print(log(e, e) == exp(0))

from math import ceil, floor, trunc
x = 1.4
y = 2.6
print(floor(x), floor(y))
print(floor(-x), floor(-y)) #el entero máas grande
print(ceil(x), ceil(y)) #devuelve el entero pequeño
print(ceil(-x), ceil(-y)) #Entero mas pequeño >= 0
print(trunc(x), trunc(y)) #valor truncado a un entero
print(trunc(-x), trunc(-y)) 

#EJERCICIOS RANDOM
from random import random, seed
seed(0) #establece la semilla con la hora actual
for i in range(5):
    print(random())

from random import randrange, randint
print(randrange(1), end=' ')  #randrange(fin) 
print(randrange(0, 1), end=' ') #randrange(inico, fin)
print(randrange(0, 1, 1), end=' ') #randrange(inicio, fin, incremento)
print(randint(0, 1)) #randint(izquierda, derecha)

from random import choice, sample
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

#EJERCICIOS PLATFORM
from platform import platform
print(platform())
print(platform(1))
print(platform(0, 1))

platform(aliased = False, terse = False)
#aliased → cuando se establece a True (o cualquier valor distinto a cero) puede hacer que la función presente los nombres de capa subyacentes alternativos en lugar de los comunes.
#terse → cuando se establece a True (o cualquier valor distinto a cero) puede convencer a la función de presentar una forma más breve del resultado (si lo fuera posible).

from platform import python_implementation, python_version_tuple
print(python_implementation()) #cadena de implementación
for atr in python_version_tuple(): #devuelve tupla e elementos (parte mayor de version, menor y numero de nivel de parche)
    print(atr)

#Modulos 
#import mod1
#import mod2
#import mod3

#Si se importa el modulo se debe anteponer el nombre de la entidad empleando la notacion con punto
#import my_module

#PIP
#pip help operación_o_comando â muestra una breve descripción de pip.
#pip list â muestra una lista de los paquetes instalados actualmente.
#pip show nombre_del_paquete â muestra información que incluyen las dependencias del paquete.
#pip search cadena â busca en los directorios de PyPI para encontrar paquetes cuyos nombres contengan cadena.
#pip install nombre â instala el paquete nombre en todo el sistema (espera problemas cuando no tengas privilegios de administrador).
#pip install --user nombre â instala nombre solo para ti; ningún otro usuario de la plataforma podrá utilizarlo.
#pip install -U nombre â actualiza un paquete previamente instalado.
#pip uninstall nombre â desinstala un paquete previamente instalado.
