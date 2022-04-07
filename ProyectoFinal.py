#Proyecto final
class Usuarios:
    def __init__ (self,nombre,contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

    def __str__(self):
        return 'Usuario: {}\nContraseña: {}\n'.format(self.nombre,self.contraseña)

#Objetos
usuario = []
print('Generando usuarios...')
enombre = ['ncastro14','jfranco17','rcalderon02']
econtraseña = ['castro123','franco123','calderon123']

for u in usuario:
    print(u)

z=0
while (z<1):
    cor = input('Ingresa tu nombre de usuario: ')
    con = input('Ingresa una contraseña:')
    print()
    u = Usuarios(cor,con)
    usuario.append(u)
    z+=1

#Fichero pickle
import pickle
f=open('Usuarios.txt','wb')
pickle.dump(usuario, f)
f.close()

f = open('Usuarios.txt','rb')
usuario = pickle.load(f)
f.close()

print('Se ha generado el usuario exitosamente.')

#Menú de opciones
print()
mo = ('Menú de opciones.\n1. Cambiar nombre de usuario.\n2. Cambio de contraseña.\n3. Eliminar usuario\n4. Salir del menú de opciones.\n')
print(mo)

while True:
    try:
        m = int(input("Ingrese un número del menú de opciones: "))
    except ValueError:
        print("Debe ingresar solo números.\n")
    else:
        if m in [1,2,3,4]:
        #Cambiar nombre de usuario 
            if m == 1:
                ncor = input('Ingresa un nuevo nombre de usuario: ')
                cor = ncor
                print(usuario,'Cambio exitoso.\n')
                print(mo)
            #Cambio de contraseña
            elif m == 2:
                ncon = input('Ingresa una nueva contraseña: ')
                con = ncon
                print(usuario,'Cambio exitoso.\n')
                print(mo)
            #Eliminar usuario
            elif m == 3:
                usuario = None
                print('Se ha eliminado el usuario exitosamente.\n')
                print(mo)
            #Salir
            else:
                print('Usted ha salido del menú.\n')
                break
        else:
            print('Debe ingresar un número del menú de opciones.\n')
        


        




        

