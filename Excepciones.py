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
