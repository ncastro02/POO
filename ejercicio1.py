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

from math import e, exp, log #Euler, exponente, logaritmo
print(pow(e, 1) == exp(log(e))) #e = constante aproximada del número Euler
print(pow(2, 2) == exp(2 * log(2))) #pow encuentra el valor de (x, y) = x^y
print(log(e, e) == exp(0))

#ceil(x) → devuelve el entero más pequeño mayor o igual que x.
#floor(x) → el entero más grande menor o igual que x.
#trunc(x) → el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).