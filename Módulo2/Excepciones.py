#Ejemplo sin excepciones
#print(1/0)

#Ejemplo1
#a=1
#b=0
#d=a/b
#print(d)

#ZeroDivisionError
a=10
#b=5
b=0
result=0
try:
    result=a/b
except ZeroDivisionError:
    print('!No se puede divir entre cero!')
print("Resultado ->", result)

#Exception
a=10
#b=5
b=0
result=0
try:
    result=a/b #result=10/5
except Exception:
    print('Operación matematica NO aceptada')
print("Resultado ->", result)

#ZeroDivisionError y Exception
a=10
#b=5
b=0
result=0
try:
    result=a/b 
except ZeroDivisionError:
    print('!No se puede divir entre cero!')
except Exception:
    print('Operación matematica NO aceptada')
finally:
    print("Buen día")
    print('m&m')
print("Resultado ->", result)

a=10
#b=5
b=0
try:
    print('Operando.....')
    result = a/b
except ZeroDivisionError:
    print('!No se puede divir entre cero!')
except Exception:
    print('Operación matematica NO aceptada')
finally:
    print("Buen día")
print("Resultado ->", result)

#Clase2

def division(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print('!No se puede dividir por cero!')
    else:
        print(result)
    finally:
        print('****************')
        print('M&M')

        print("Ejemplo 1 ->")
        divisions(5,0)
        print("Ejemplo 2 ->")
        divisions(5,2)

while True:
    try:
        x= int(input("Indica un número: "))
        break
    except ValueError:
        print("OOps! No es un número válido. Intenta de nuevo...")
    else:
        print("Perfecto, indicaste un digito")
        break

try:
    f = open('Empleados.txt') #Inexistente
except FileNotFoundError:
    print('¡El fichero no existe!')
else:
    print(f.read())

