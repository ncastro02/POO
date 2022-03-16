#Cadenas
#Ejemplo conteo de caracteres
word = 'by'
print(len(word)) #len cuenta el no. de caracteres(2)

empty = ''
print(len(empty)) #(0)

i_am = 'I\'m'
print(len(i_am)) #(3)

multiline = '''Línea #1 
Línea #2''' #El caracter invisible es el espacio en blanco (\n)
print(len(multiline)) #(17)

#Ejemplo operaciones con cadenas
str1 = 'a'
str2 = 'b'
print(str1 + str2) #ab
print(str2 + str1) #ba
print(5 * 'a') #aaaaa
print('b' * 4) #bbbb

# La función ord ().
char_1 = 'a'
char_2 = ' '  # space
print(ord(char_1))
print(ord(char_2))

# Demostración de la función chr.
print(chr(97)) 
print(chr(945))

# Indexando cadenas.
the_string = 'silly walks'
for ix in range(len(the_string)):
    print(the_string[ix], end=' ')
print()

# Iterando a través de una cadena.
the_string = 'silly walks'
for character in the_string:
    print(character, end=' ')
print()

# Rebanadas
alpha = "abdefg"
print(alpha[1:3]) #bd
print(alpha[3:]) #efg
print(alpha[:3]) #abd
print(alpha[3:-2]) #e
print(alpha[-3:4]) #e
print(alpha[::2]) #adf
print(alpha[1::2]) #beg

alphabet = "bcdefghijklmnopqrstuvwxy"
alphabet = "a" + alphabet
alphabet = alphabet + "z"
print(alphabet) 

# Demonstrando min() - Ejemplo 1:
print(min("aAbByYzZ"))
# Demonstrando min() - Ejemplo 2 y 3:
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')
t = [0, 1, 2]
print(min(t))

# Demostración de max() - Ejemplo 1:
print(max("aAbByYzZ"))
# Demostración de max() - Ejemplo 2 & 3:
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']')
t = [0, 1, 2]
print(max(t))

# Demonstrando el método index():
print("aAbByYzZaA".index("b")) #Busca la secuencia desde el principio
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demostración de la función list():
print(list("abcabc"))
# Demostración de la función list():
print("abcabc".count("b"))
print('abcabc'.count("d"))

#Los operadores in y not in
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet) #True
print("F" in alphabet) #False
print("1" in alphabet) #False
print("ghi" in alphabet) #True
print("Xyz" in alphabet) #False

#Resumen de métodos de cadenas
#capitalize(): cambia todas las letras de la cadena a mayúsculas.
#center(): centra la cadena dentro de una longitud conocida.
#count(): cuenta las ocurrencias de un carácter dado.
#join(): une todos los elementos de una tupla/lista en una cadena.
#lower(): convierte todas las letras de la cadena en minúsculas.
#lstrip(): elimina los caracteres en blanco al principio de la cadena.
#replace(): reemplaza una subcadena dada con otra.
#rfind(): encuentra una subcadena comenzando por el final de la cadena.
#rstrip(): elimina los caracteres en blanco al final de la cadena.
#split(): divide la cadena en una subcadena usando un delimitador dado.
#strip(): elimina los espacios en blanco iniciales y finales.
#swapcase(): intercambia las mayúsculas y minúsculas de las letras.
#title(): hace que la primera letra de cada palabra sea mayúscula.
#upper(): convierte todas las letras de la cadena en letras mayúsculas.

# Demostración del método capitalize():
print('aBcD'.capitalize()) #Abcd
# Demostración del método center():
print('[' + 'alpha'.center(10) + ']')
# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")
# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))

# Demostración del método the isalnum():
print('lambda30'.isalnum()) #True
print('lambda'.isalnum()) #True
print('30'.isalnum()) #True
print('@'.isalnum()) #False
print('lambda_30'.isalnum()) #False

# Ejemplo 1: Demostración del método isapha():
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Ejemplo 2: Demostración del método isdigit():
print('2018'.isdigit())
print("Year2019".isdigit())

# Ejemplo 1: Demostración del método islower():
print("Moooo".islower())
print('moooo'.islower())

# Ejemplo 2: Demostración del método isspace(:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Ejemplo 3: Demostración del método isupper():
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))

# Demostración del método lower():
print("SiGmA=60".lower())

# Demostración del método the lstrip():
print("[" + " tau ".lstrip() + "]")

# Demostración del método replace():
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

#Cadenas 
'10' == '010' #False
'10' > '010' #True
'10' > '8' #False
'20' < '8' #True
'20' < '80' #True

# Demostración de la función sorted():
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)
print(first_greek)
print(first_greek_2)
print()

# Demostración del método sort():
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)
second_greek.sort()
print(second_greek)

# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)
print(cipher)
