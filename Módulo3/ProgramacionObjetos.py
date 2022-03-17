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
