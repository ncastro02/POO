#Cadenas y ejemplos
mensaje1 = str.capitalize('Esto es una PRUEBA de capitalize')
print(mensaje1)

mensaje2 = 'otra Prueba de capitalize'.capitalize()
print(mensaje2)

mensaje3 = 'Tercera y última de capitalize'
print(mensaje3.capitalize())

#lower, upper, title, swapcase
texto=input("Introduzca un texto: ")
print("Aplicando lower() al texto: ",texto.lower())
print("Aplicando upper() al texto: ",texto.upper())
print("Aplicando title() al texto: ",texto.title())
print("Aplicando capitalize() al texto: ",texto.capitalize())
print("Aplicando swapcase()) al texto: ",texto.swapcase())

palabra = input("Introduzca la frase: ")
print("No. de Palabras", palabra.count(palabra))
print("No. de caracteres ", len(palabra))

#Subcadena
texto= input("Introduzca la frase: ")
palabra= input("Introduzca la letra o palabra para obtener el no. de veces que aparece: ")
nva= texto.count(palabra)
if nva > 1:
    print("La palabra/letra '{}' aparece {} veces".format(palabra, nva))
elif nva ==1:
    print("La palabra/letra '{}' aparece {} vez".format(palabra, nva))
else:
    print("La palabra/letra '{}' no aparece en el texto".format(palabra))

#Tamaño de una cadena
texto= input("Introduzca una frase:")
tamaño =len(texto)
if tamaño > 1:
    print("La frase tiene {} caracteres".format(tamaño))
elif nva ==1:
    print("La frase tiene {} caractér".format(tamaño))
else:
    print("No ha introducido una frase")

#startswith() endswith()
texto= input("Introduzca un texto:")
ep= input("Introduzca la letra/palabra o frase que estaría al inicio ")
ap= input("Introduzca la letra/palabra o frase que estaría al final")

#Comprobamos si el texto empieza por el input ep
if texto.startswith(ep):
    print("El texto introducido empieza por ", ep)
else:
    print("El texto introducido no empieza por ", ep)

#Comprobamos si el texto acaba por el input ap
if texto.endswith(ap):
    print("El texto introducido acaba por ", ap)
else:
    print("El texto introducido no acaba por ", ap)
