from io import open
texto = 'Una línea con texto\nOtra línea con texto'
#Ruta donde creamos el fichero, w indica escritura(puntero al principio)
fichero= open('fichero.txt','w')

#Escribimos el texto
fichero.write(texto)
#Cerramos el fichero
fichero.close()

texto='Una línea con texto\nOtra línea con texto\nTexto3\nTexto4'
texto2='Una línea con texto\nOtra línea con texto\nTexto3\nTexto4'
#Ruta donde leeremos el fichero, r indica letura (por defecto ya es r)
fichero = open('fichero.txt','r')
#Lectura completa
fichero.write(texto)
fichero.write(texto2)
#Cerramos el fichero
fichero.close()

#Ruta donde leeremos el fichero, r indica letura (por defecto ya es r)
try:
    fichero = open('fichero.txt','r')
    #Lectura completa
    texto = fichero.read()
    #Cerramos el fichero
    fichero.close()
except Exception:
    print('Error no existe el archivo')
else:
    print(texto)

#Creamos un fichero de prueba con 4 líneas
fichero=open('fichero2.txt','w')
texto='Línea 1\nLínea2\nLínea3\nLínea4'
fichero.write(texto)
fichero.close()

#Lo abrimos en lectura con escritura y escribimos algo
fichero = open('fichero2.txt','r+')
fichero.write('0123456\n')
fichero.write('78944561')

#Volvemos a poner el puntero al inicio y leemos hasta el final
fichero.seek(0)
fichero.read()
fichero.close()

print(fichero)

#Creamos una clase de prueba
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def _str__(self):
        return 'Nombre {} ,Edad {}'.format(self.nombre,self.edad)

#Creamos la lista con los objetos
nombres=['Hector','Mario','Marta','Sofía','Mónica']
edad = [25,30,35,40,45]
personas=[]

z=0
for n in nombres:
    p=Personas(n,edad[z])
    personas.append(p)
    z+=1

#EScribamos la lista en el fichero con pickle
import pickle
f=open('personas.txt','wb')
pickle.dump(personas, f)
f.close()

#Leemos la lista del fichero con pickle
f=open('personas.txt','rb')
personas =pickle.load(f)
f.close()
for p in personas:
    print(p)

#Creamos la lista con los objetos
personas=[]
z=0
while (z<5):
    nom = input('Nombre:')
    edad=int(input('Edad:'))
    p=Personas(nom,edad)
    personas.append(p)
    z+=1

#EScribamos la lista en el fichero con pickle
import pickle
f=open('personas2.txt','wb')
pickle.dump(personas, f)
f.close()

#Leemos la lista del fichero con pickle
f=open('personas2.txt','rb')
personas =pickle.load(f)
f.close()
for p in personas:
    print(p)

from io import open
import pickle

class Pelicula:
    #Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la pelicula;', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo,self.lanzamiento)

class Catalogo:
    peliculas =[]
    #Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas)== 0:
            print('El catalogo esta vacio')
            return
        for p in self.peliculas:
            print(p)

    def cargar(self):
        fichero=open('catalogo.txt','ab+')
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print('El fichero esta vacío')
        finally:
            fichero.close()
            print('Se han cargado {} peliculas'.format(len(self.peliculas)))

    def  guardar(self):
        fichero =open('catalogo.txt','wb')
        pickle.dump(self.peliculas,fichero)
        fichero.close()

#Creamos un catalogo
c = catalogo()
#Mostramos el contenido
c.mostrar()
#Agregamos una pelicula
c.agregar(pelicula('El Padrino'),175,1972)
c.agregar(pelicula('El Padrino: parte 2'),202,1974)
c.agregar(pelicula('El Examen'),100,2005)

#Mostramos el catalogo de nuevo 
c.mostrar()
del(catalogo)