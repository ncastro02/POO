#herencia
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
        self.emisor=emisor
        super().__init__(numero,cuentah,caducidad,estado,cantidad)
        return

    def __str__(self):
        return Tarjeta.__str__(self)+ '\nTipo de tarjeta {} \n Emisor: {}  '.format(self.tipo, self.emisor)
deb = Debito ('9110001','Angélica María','05/26','Inactiva','Debito','Visa',2500)
deb.activar()
print(deb.emisor)
print(deb.cuentahabiente)
deb.deposito(1000)

class Credito (Tarjeta):
    def __init(self,numero,cuentah,caducidad,estado,tipo,cantidad=0):
        self.tipo =tipo
        self.emisor =emisor
        self.limite =limite
        super().__init__(numero,cuentah,caducidad,estado,cantidad)
        return

    def __str__(self):
        return Tarjeta.__str__(self) + '\nTipo de Tarjeta {} \n Emisor: {} \n Limite de Crédito: $ {}'.format(self.tipo, self.emisor, self.limite)
tdc=Credito('9110001','Angélica María','05/26','Inactiva','Debito','Visa',2500)
tdc.activar()

class Puntos(Tarjeta):
    def __init(self,numero,cuentah,caducidad,estado,tipo,cantidad=0):
        self.tipo =tipo
        super().__init__(numero,cuentah,caducidad,estado,cantidad)
        return

    def __str__(self):
        return Tarjeta.__str__(self) + '\nTipo de Tarjeta {} '.format(self.tipo)
puntos=Puntos('9110001','Angélica María','05/26','Inactiva','Debito','Visa',2500)
print(puntos)
puntos.acitvar()

#Vehiculo
class Vehiculo():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color,self.ruedas)

class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindro):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidadself.cilindro = cilindro

    def __str__(self):
        return "Color {}, {} km/h, {} ruedas, {} cc".format(self.color, self.velocidad,self.ruedas,self.cilindro)

coche = Coche("azul",4,150,1200)
print(coche)
