#
class Tarjeta:
    def _init__(self, numero, cuentah, caducidad, estado, cantidad =0):
        self.numero = numero
        self.cuentahabiente = cuentah
        self.caducidad = caducidad
        self.estado = estado
        self.saldo = saldo
        return

def _str__(self):
    return 'Tarjeta número {} del derechohabitante {} tiene una fecha de expiración {}, estado de la cuenta {}, cuenta con un saldo ${}'.format(self.numero, self.cuentahabitante, self.caducidad, self.estado,str(self.saldo))

def deposito(self, cantidad):
    self.saldo += cantidad
    #self.saldo = self.saldo + cantidad
    return 'El saldo nuevo de la tarjeta es {}'.format(self.saldo)

def retirar(self, cantidad):
    if self.saldo < cantidad:
        msg = 'Saldo Insuficiente para el retiro'
    else:
        self.saldo -= cantidad
        msg = 'El saldo nuevo de la tarjeta es {}'.format(self.saldo)
    print(msg)

def mostrar_saldo(self):
    #return 'el saldo actual de la cuenta: ',self.saldo
    print('El saldo actual de la cuenta es: $',self.saldo)

def activar(self):
    self.estado ='Activa'
    return

def anular (self):
    self.estado ='Activa'
    return

class Debito(Tarjeta):
    def __init__(self,numero,cuentah,caducidad, estado,tipo,cantidad=0):
        self.tipo =tipo
        super().__init__(numero,cuentah,caducidad,estado,cantidad)
        return

    def __str__(self):
        return Tarjeta.__str__(self)+ '\nTipo de tarjeta {} '.format(self.tipo)

class Credito (Tarjeta):
    def __init(self,numero,cuentah,caducidad,estado,tipo,cantidad=0):
        self.tipo =tipo
        super().__init__(numero,cuentah,caducidad,estado,cantidad)
        return

    def __str__(self):
        return Tarjeta.__str__(self + '\nTipo de Tarjeta {} '.format(self.tipo))        

t=Tarjeta('110010', 'Juan Lopez', '05/23', 'Inactiva', 3)
t1=Tarjeta('110011', 'Monica Naranjos', '05/23', 'Inactiva',0)
t2=Tarjeta('110012', 'JPedro García', '05/23', 'Inactiva', 3000)

print(t)
print('**************')
print(t1)
print('**************')
print(t2)

t.activar()
t1.activar()
t2.activar()

t.deposito(200)
t1.deposito(400)
t2.deposito(600)
t.retirar(800)
t.retirar(80)

print("Bienvenido al menú interactivo")
while(True):
    print("""¿Qué quieres hacer? Escribe una opción
    1) Agregar monto
    2)Retiro monto
    3)Mostrar Saldo
    4)Activar tarjeta
    5)Inactivar tarjeta
    6)Salir""")
    opcion = input()
    if opcion == '1':
        monto=float(input("Indica el monto a agregar: "))
        t.deposito(monto)
    elif opcion == '2':
        monto=float(input("Indica el monto a retirar: "))
        t.retirar(monto)
    elif opcion == '3':
        t.mostrar_saldo()
    elif opcion == '4':
         t.activar()
         print(t)
    elif opcion == '5':
         t.Inactivar()
         print(t)
    elif opcion == '6':
         print("¡Hasta luego! Ha sido un placer ayudarte")
         break
    else:
        print("Comando desconocido, vuelve a intentarlo")

#ejercicio
class Coche():
    ruedas=4
    color="azul"
    def encendido(self):
        print("El carro esta encendido")
    def desplazamiento(self):
        print("El coche se esta desplazando sobre 4 ruedas")
    def apagado(self):
        print("El carro esta apagado")

class Moto():
    ruedas=2
    def encendido(self):
        print("La moto esta encendido")
    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")
    def apagado(self):
        print("La moto esta apagada")

miVehiculo=Coche()
print("Mi coche tiene ", miVehiculo.ruedas, " ruedas")
print("Mi coche de color ", miVehiculo.color)
miVehiculo.encendido()
miVehiculo.desplazamiento()
miVehiculo.apagado()

print("------------Segundo Objeto------------")
miVehiculo2=coche()
print("Mi coche tiene ", miVehiculo2.ruedas, " ruedas")
print("Mi coche de color ", miVehiculo2.color)
miVehiculo2.encendido()
miVehiculo2.desplazamiento()
miVehiculo2.apagado() 

#Ejercicio cachorro
class Cachorro():
    def __init__(self,color,raza,tamaño):
        self.color=color
        self.raza=raza
        self.tamanio=tamanio
    def __str__(self):
        return """\
Raza: {}
Color: {}
Tamaño: {} """.format(self.raza, self.color, self.tamanio)
perrito=Cachorro("Marron claro", "Golden retriever","Mediano")
print(perrito)

lista =[]
lista.append(Cachorro("Marron claro", "Golden retriever","Mediano"))
lista.append(Cachorro("Gris", "Golden retriever","Mediano"))
lista.append(Cachorro("Negro", "Golden retriever","Mediano"))
lista.append(Cachorro("Blanco", "Golden retriever","Mediano"))

#for x in lista:
#   print(print(lista[x]))

class Cachorro2():
    def __init__(self):
        perritos = []
    def agregar(self,color,raza,tamaño):
        self.perritos.append(color)
    def __str__(self):
        return """\
Color: {} """.format(self.color)
perrito=Cachorro2("Marron claro")
print(perrito)

lista =[]
lista.append(Cachorro2("Marron claro"))
lista.append(Cachorro2("Gris"))
lista.append(Cachorro2("Negro"))
lista.append(Cachorro2("Blanco"))

for lista in len(lista):
    print(lista[x])
