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

#Herencia Múltiple clase 2
class Empleado:
    def __init__(self,nombre,iden,genero):
        self.nombre = nombre
        self.iden = iden
        self.genero = genero

class Provincia:
    domicilio = 'Valencia'

class RecHumanos(Empleado,Provincia):
    def saludo(self):
        print("Hola, mi nombre es " + self.nombre + " y mi ID es " + self.iden + ".")
        print("Trabajo en Recursos Humanos.")
        if self.genero == 'F':
            print("Genero Femenino.")
        else:
            print("Genero Masculino.")
        print("Vivo en " + self.domicilio + ".")

empleado1 = RecHumanos("Karla", "182052", "F")
empleado1.saludo()
print("*************")
empleado2=Tecnologias("Pedro","182053","M")
empleado2.saludo()

#Mismo ejemplo object
class Empleado(object):
    def __init__(self,nombre,iden,genero):
        self.nombre = nombre
        self.iden = iden
        self.genero = genero

class Provincia(object):
    domicilio = 'Valencia'

class RecHumanos(Empleado,Provincia):
    def saludo(self):
        print("Hola, mi nombre es " + self.nombre + " y mi ID es " + self.iden + ".")
        print("Trabajo en Recursos Humanos.")
        if self.genero == 'F':
            print("Genero Femenino.")
        else:
            print("Genero Masculino.")
        print("Vivo en " + self.domicilio + ".")

empleado1 = RecHumanos("María", "182052", "F")
empleado1.saludo()
print("*************")
empleado2=Tecnologias("Juan","182053","M")
empleado2.saludo()

class Persona(object):
    """Clase que representa una Persona"""

    def __init__(self,cedula,nombre,apellido,sexo):
        """Devuelve una cadena representativa de Persona"""
        return "%s: $s, $s $s, $s" % (
            self.__doc__[25:34], str(self.cedula), self.nombre,self.apellido, self.getGenero(self.sexo))

def hablar(self, mensaje):
    """Mostrar mensaje de salud de Persona"""
    genero = ("Masculino","Femenino")
    if sexo == "M":
        return genero[0]
    elif sexo == "F":
        return genero[1]
    else:
        return "Desconocido"

persona1 = Persona("V-13458796", "Leonardo","Caballero","M")
persona2 = Persona("V-23569874","Ana","Poleo","F")

class Supervisor(Persona):
    """Clase que representa a un Supervisor"""

    def __init__(self,cedula,nombre,apellido,sexo,rol):
        """Constructor de clase Supervisor"""

        #Invoca al constructor de clase Persona
        Persona.__init__(self,cedula,nombre,apellido,sexo)
        #Nuevos atributos
        self.rol = rol
        self.tareas = ["10","11","12","13"]

    def __str__(self):
        """Devuelve una cadena representativa al Supervisor"""
        return "%s: %s %s, rol: '%s', sus tareas: %s." %(
            self.__doc__[26:37], self.nombre, self.apellido, self.rol, self.consulta_tareas())

    def consulta_tareas(self):
        """Mostrar las tareas del Supervisor"""
        return ','.join(self.tareas)

supervisor1= Supervisor("V-16987456","Jen","Paz","D","Administrador")
print(supervisor1)

print("\n" + str(supervisor1) + "\n")
print("- Cedula de identidad: {0}.".format(supervisor1.cedula))
print("- Nombre completo: {0} {1}.".format(supervisor1.nombre, supervisor1.apellido))
print("- Genero: {0}.".format(supervisor1getGenero(supervisor1.sexo)))
print("- {0} {1} dijo: {2}".format(supervisor1.nombre,supervisor1.apellido, supervisor1.hablar("¡A trabajar Leonardo!!!".upper)))
